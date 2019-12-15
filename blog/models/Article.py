from blog.models import connect_db
from datetime import datetime


class Article():


    def __init__(self, title, content, date_created, public=True, id=None):
        self.id           = id
        self.title        = title
        self.content      = content
        self.date_created = date_created
        self.public       = public


    def __repr__(self):
        return ("<Article id={self.id}, title='{self.title}'>".format(self=self))

    def store(self):
        """Saves article to database"""

        data = {
                "title"        : self.title,
                "content"      : self.content,
                "public"       : self.public,
                "date_created" : self.date_created
        }

        with connect_db() as conn:

            c = conn.cursor()

            if not self.id:
                sql = """
                    insert into Article(
                        title, content, date_created, public
                    ) values (
                        :title, :content, :date_created, :public
                    );"""

                c.execute(sql, data);
                self.id = c.lastrowid

            else:
                data["id"] = self.id
                sql = """
                    update Article set
                        title        = :title,
                        content      = :content,
                        date_created = :date_created,
                        public       = :public
                    where id=:id;"""

                c.execute(sql, data)

            conn.commit()

    def delete(self):
        """Removes article from database"""
        with connect_db() as conn:
            c = conn.cursor()
            sql = """delete from Article where id=?"""
            c.execute(sql, [str(self.id)])
            conn.commit()



    @staticmethod
    def title_exists(title):
        """Return whether input title is already in use as a boolean"""

        with connect_db() as conn:
            c = conn.cursor()
            sql = "select 1 from Article where title=?"
            c.execute(sql, [title])


            return c.fetchone() != None

    @staticmethod
    def get_amount():
        """returns the amount of articles that are currently stored"""
        with connect_db() as conn:
            c = conn.cursor()
            sql = "select count() from Article"
            c.execute(sql)
            return c.fetchone()[0]

    @staticmethod
    def get_by_id(id):
        """Returns article with id matching the input. Returns None if id doesn't exist"""
        with connect_db() as conn:
            c = conn.cursor()
            sql = "select * from Article where id=?"
            c.execute(sql, [str(id)])
            result = c.fetchone()

        if result != None:
            return Article.create_object(result)
        else:
            return None

    @staticmethod
    def get_latest(amount=1, offset=1, include_private=False):
        """Returns a list of articles sorted by date in descending order"""
        with connect_db() as conn:
            c = conn.cursor()
            sql = """
                select * from Article
                {where}
                limit ? offset ?
                order by date_created desc
            """

            if include_private:
                sql = sql.format(where=" ")
            else:
                sql = sql.format(where="where public=1")

            c.execute(sql, (amount, offset))
            return [Article.create_object(result) for result in c.fetchall()]


    @staticmethod
    def get_all():
        """Returns a list of all articles currently stored in database"""
        with connect_db() as conn:
            c = conn.cursor()
            sql = "select * from Article order by date_created desc"
            c.execute(sql)

            return [Article.create_object(result) for result in c.fetchall()]

    @staticmethod
    def create_object(result):
        """Static method that creates an Article object from the sql query results"""
        return Article(
            id            = result[0],
            title         = result[1],
            content       = result[2],
            date_created  = result[3],
            public        = result[4],
        )

    @staticmethod
    def convert_date(date_created, pretty=False):
        """Returns input datetime converted to human readable string"""

        if pretty:
            date_format = "%A %d %B %Y, %H:%M"
        else:
            date_format = "%H:%M %d/%m/%Y"

        return datetime.strftime(date_created, date_format)







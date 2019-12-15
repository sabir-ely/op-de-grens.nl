from blog.models import connect_db


def get_text():
    """Returns Description text"""
    with connect_db() as conn:
        c = conn.cursor()
        c.execute("select content from Description where id=1")
        return c.fetchone()[0]

def set_text(text):
    """Changes Description text"""
    with connect_db() as conn:
        c = conn.cursor()
        c.execute("update Description set content=?", [text])
        conn.commit()

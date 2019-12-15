const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {

    entry: {
        admin  : './blog/static/src/adminEntry.ts',
        public : './blog/static/src/publicEntry.ts',

    },
    output: {
        filename: './blog/static/dist/[name].js'
    },

    resolve: {
        extensions: ['.ts', '.tsx', '.js']
    },

    module: {
        rules : [
            {
                test: /\.tsx?$/,
                loader: 'ts-loader',
                options : {
                    transpileOnly : true,
                }
            },
            {
                test: /\.s?css$/,
                loader: ['style-loader','css-loader', 'sass-loader']
            }
        ]
    },

    plugins : [
        new UglifyJSPlugin({
            compress : true,
        }),
    ]
}

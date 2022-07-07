var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var extractPlugin = new ExtractTextPlugin({
    filename: 'django_arpartners/portfolio/static/css/main.bundle.css',
    allChunks: true
});

module.exports = {
    entry: ['./django_arpartners/portfolio/static/js/index.js', './django_arpartners/portfolio/static/css/styles.scss'],
    output: {
        path: path.resolve(__dirname, 'django_arpartners/portfolio/static/js/'),
        filename: 'django_arpartners/portfolio/static/css/bundle.js',
        publicPath: '/'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: [
                    {
                        loader: 'babel-loader',
                        options: {
                            presets: ['es2015']
                        }
                    }
                ]
            },
            {
                test: /\.scss$/,
                use: extractPlugin.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'sass-loader']
                })
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'django_arpartners/portfolio/static/css/fonts/',
                            publicPath: 'django_arpartners/portfolio/static/css/fonts/'
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        extractPlugin
    ]
};

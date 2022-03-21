const path = require('path');

module.exports = {
  entry: './index.js',
  output: {
    path: path.resolve(__dirname, 'library_app\\library\\static'),
    filename: 'webpack.bundle.js',
  },
  devtool: 'source-map'
};
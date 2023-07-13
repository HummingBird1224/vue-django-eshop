const path = require("path");
const glob = require("glob");
const BundleTracker = require('webpack-bundle-tracker');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const { VueLoaderPlugin } = require("vue-loader");
const exec = require('child_process').exec;

const env = process.env.NODE_ENV;

// 動的にエントリーファイルを設定.
const entryDir = '../static_files/static/js/templates';
const entries = {};

glob.sync("*.js", {cwd: entryDir}).map(function (file) {
  const key = path.parse(file).name;
  entries[key] = path.resolve(entryDir, file);
});

module.exports = {
  context: __dirname,
  mode: env,
  entry: entries,
  output: {
    filename: "[name]-[contenthash].js",
    path: path.resolve('../static_files/static/bundles/'),
    publicPath: ''
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new CleanWebpackPlugin(),
    new VueLoaderPlugin(),
    {
      apply: (compiler) => {
        compiler.hooks.afterEmit.tap('AfterEmitPlugin', (compilation) => {
          exec('echo "json update" && docker exec canal_server python /suez/src/manage.py collectstatic --noinput', (err, stdout, stderr) => {
            if (stdout) process.stdout.write(stdout);
            if (stderr) process.stderr.write(stderr);
          });
        });
      }
    }
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.scss$/,
        use: [
          { loader: 'vue-style-loader' },
          { loader: 'style-loader' },
          { loader:  'css-loader'},
          { loader:  'sass-loader',
            options: {
              implementation: require('sass'),
            }
          },
        ]
      },
      {
        test: /\.css$/,
        use: [
          "vue-style-loader",
          'style-loader',
          {
            loader: 'css-loader',
            options: {
              url: false,
              sourceMap: true
            }
          }
        ]
      },
    ]
  },

  resolve: {
    extensions: ['.js', '.vue'],
    modules: [
      "node_modules"
    ],
    alias: {
      'vue': path.resolve('./node_modules/vue/index.js'),
      'axios': path.resolve('./node_modules/axios/dist/axios.js'),
      'js-cookie': path.resolve('./node_modules/js-cookie/src/js.cookie.js'),
      'vee-validate': path.resolve('./node_modules/vee-validate/dist/vee-validate.js'),
      '@vee-validate/rules': path.resolve('./node_modules/@vee-validate/rules/dist/vee-validate-rules.js'),
      '@vee-validate/i18n': path.resolve('./node_modules/@vee-validate/i18n/dist/'),
      'vue3-smooth-scroll': path.resolve('./node_modules/vue3-smooth-scroll/dist/vue-smooth-scroll.min.js'),
      'swiper': path.resolve('./node_modules/swiper'),
      'sanitize-html': path.resolve('./node_modules/sanitize-html/dist/sanitize-html.min.js'),
      'fabric': path.resolve('./node_modules/fabric/dist/fabric.min.js'),
      'jspdf': path.resolve('./node_modules/jspdf/dist/jspdf.min.js'),
      'rgbaster': path.resolve('./node_modules/rgbaster/dist/rgbaster.js'),
      'regenerator-runtime': path.resolve('./node_modules/regenerator-runtime/runtime.js'),
      'vueperslides': path.resolve('./node_modules/vueperslides'),
      'yup': path.resolve('./node_modules/yup'),
      'yup-locale-ja': path.resolve('./node_modules/yup-locale-ja'),
    }
  }
};

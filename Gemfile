source 'http://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages'], group: :jekyll_plugins
gem 'jekyll-redirect-from', versions['jekyll-redirect-from'], group: :jekyll_plugins

# gem 'github-pages', '206', group: :jekyll_plugins
# gem 'jekyll-redirect-from', '0.15.0', group: :jekyll_plugins

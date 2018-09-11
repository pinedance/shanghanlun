source 'https://rubygems.org'
# source "http://rubygems.org"
# source "http://mirror.ops.rhcloud.com/mirror/ruby/"
# source "http://ruby.taobao.org" # not available
# source "http://gems.ruby-china.org/"
# source "http://gems.cloudafrica.net" # not available
# source "http://tokyo-m.rubygems.org"  # not available

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages'], group: :jekyll_plugins
gem 'jekyll-redirect-from', versions['jekyll-redirect-from'], group: :jekyll_plugins

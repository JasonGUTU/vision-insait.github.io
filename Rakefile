# frozen_string_literal: true

ENV["LC_ALL"] = "en_US.UTF-8"
ENV["LANG"] = "en_US.UTF-8"

JEKYLL_CONFIG = "_config.yml,_config.dev.yml"
JEKYLL_CONFIG_PROD = "_config.yml"

desc "Build site (production / GitHub Pages paths, UTF-8 locale)"
task :build do
  sh "bundle exec jekyll build --config #{JEKYLL_CONFIG_PROD}"
end

desc "Build locally (same asset paths as GitHub Pages)"
task "build:local" do
  sh "bundle exec jekyll build --config #{JEKYLL_CONFIG}"
end

desc "Serve at http://127.0.0.1:4000/vision-insait.github.io/"
task :serve do
  sh "bundle exec jekyll serve --livereload --config #{JEKYLL_CONFIG}"
end

task default: :build

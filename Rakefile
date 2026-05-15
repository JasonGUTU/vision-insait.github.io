# frozen_string_literal: true

ENV["LC_ALL"] = "en_US.UTF-8"
ENV["LANG"] = "en_US.UTF-8"

desc "Build site (UTF-8 locale for template asset paths)"
task :build do
  sh "bundle exec jekyll build"
end

desc "Serve locally"
task :serve do
  sh "bundle exec jekyll serve --livereload"
end

task default: :build

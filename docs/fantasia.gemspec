Gem::Specification.new do |spec|
  spec.name     = "fantasia"
  spec.version  = "1.0"
  
  spec.authors  = ["Sander Schulhoff, Others..."]
  
  spec.summary  = "A theme built for gym and pettingzoo"
  spec.homepage = ""
  spec.license  = "MIT"
  spec.files    = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^(assets|_(data|includes|layouts|sass)/|(LICENSE|README|index|404|legal)((\.(txt|md|markdown|html)|$)))}i)
  end

  spec.required_ruby_version = '>= 2.5.0'
  spec.add_development_dependency "bundler", "~> 2.0"
  spec.add_development_dependency "rake", "~> 13.0"
end

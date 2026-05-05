package trivy.dependency

# Allowed packages
allowed = {
  "express",  
  "lodash",
  "jsonwebtoken",
  "mongoose" 
}

deny[message] {
  input.Target == "node-pkg"
  not allowed[input.PkgName]

  message = sprintf(
    "Package %s is banned by dependency policy", [input.PkgName])
}

package trivy.license

# Allow List
allow_list = {
  "MIT",
  "Apache-2.0",
  "ISC"
}

deny[message] {
  not allow_list[input.License]
  message = sprintf("License %s is not permitted", [input.License])
}

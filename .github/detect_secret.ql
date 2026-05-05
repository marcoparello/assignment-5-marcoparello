import javascript


from ExportedVariable v, Property p, Literal l
where

  l = p.getValue() and
  l.getType() = "string" and

  v.getAnExportedValue() = p.getParent()

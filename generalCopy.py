def generalCopy(source, target, startSourceX, startSourceY, startTargetX, startTargetY, toCopyWidth, toCopyheight):
  """Copy a picture or portion of a picture to another picture"""
  targetX = startTargetX
  for sourceX in range(startSourceX, startSourceX + toCopyWidth):
    targetY = startTargetY
    for sourceY in range(startSourceY, startSourceY + toCopyWidth):
      sourcePx = getPixel(source, sourceX, sourceY)
      targetPx = getPixel(target, targetX, targetY)
      setColor(targetPx, getColor(sourcePx))
      targetY += 1
    targetX += 1
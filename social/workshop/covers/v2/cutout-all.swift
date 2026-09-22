import Foundation
import Vision
import CoreImage
let args = CommandLine.arguments
let inURL = URL(fileURLWithPath: args[1]); let outBase = args[2]
guard let ci = CIImage(contentsOf: inURL, options: [.applyOrientationProperty: true]) else { print("cannot load"); exit(1) }
let handler = VNImageRequestHandler(ciImage: ci, options: [:])
let req = VNGenerateForegroundInstanceMaskRequest()
try handler.perform([req])
guard let obs = req.results?.first else { print("no foreground"); exit(1) }
let ctx = CIContext()
for i in obs.allInstances {
  let masked = try obs.generateMaskedImage(ofInstances: IndexSet(integer: i), from: handler, croppedToInstancesExtent: true)
  let out = CIImage(cvPixelBuffer: masked)
  let png = ctx.pngRepresentation(of: out, format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)!
  let url = URL(fileURLWithPath: "\(outBase)-i\(i).png"); try png.write(to: url)
  print("instance", i, Int(out.extent.width), "x", Int(out.extent.height))
}

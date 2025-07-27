import exifread

def convert_to_degrees(value):
	d, m, s = [float(x.num)/float(x.den) for x in value.values]
	return d + (m/60.0)+(s/3600.0)

def extract_metadata(file_path):
	with open(file_path, 'rb')as f:
		tags = exifread.process_file(f)
	if not tags:
		print("No metadata found in this image.")
		return
	print(f"\n--- Metadata for: {file_path} ---\n")

	with open("metadata_report.txt","w") as report:
		for tag in tags:
			report.write(f"{tag}: {tags[tag]}\n")
			print(f"{tag}:{tags[tag]}")

	try:
		lat = convert_to_degrees(tags['GPS GPSLatitude'])
		lat_ref = str(tags['GPS GPSLatitudeRef'])
		lon = convert_to_degrees(tags['GPS GPSLongitude'])
		lon_ref = str(tags['GPS GPSLongitudeRef'])

		if lat_ref != "N":
			lat = -lat
		if lo_ref != "E":
			lon = -lon

		print(f"\n GPS Coordinates:")
		print(f"Latitude: {lat}")
		print(f"Longitude: {lon}")
		print(f"Google Maps: https://maps.google.com/?q={lat},{lon}")

	except KeyError:
		print("\n No GPS data found in this image.")

extract_metadata("/home/maya/Documents/project/IMG_20241012_122752.jpg")

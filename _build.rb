require "mp3info"

filelist = Dir["./mp3/*.mp3"]

urlrgx = /(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?/

filelist.each do |filename|

	puts "Detected #{filename}"

	base_name = File.basename( filename, ".mp3" )
	created_date, title = base_name.split('_')
	mdfilename = "_posts/#{created_date[0..3]}-#{created_date[4..5]}-#{created_date[6..7]}-#{title.gsub(' ', '-')}.md"

	Mp3Info.open( filename ) do |mp3|
		len_h = (mp3.length / 3600).floor
		len_m = (mp3.length / 60).floor - ( len_h * 60 )
		len_s = (mp3.length).floor - ( len_h * 3600 ) - ( len_m * 60 )
		mp3.tag2.TLEN = "#{ len_h.to_s.rjust(2, '0') }:#{ len_m.to_s.rjust(2, '0') }:#{ len_s.to_s.rjust(2, '0') }"
		script = ( mp3.tag2.COMM )? mp3.tag2.COMM : ""
		post_body = script.gsub(/\r?\n/, "\n\n").gsub(urlrgx, '[Ref](\\0)')
		ym = string = <<-FIN
---
layout: post
explicit: no
title: "#{created_date} #{ title }"
enclosure:
  type: "Audio/mp3"
  filename: "#{ base_name }"
  duration: "#{ mp3.tag2.TLEN }"
tags: ap_news
---

#{ post_body }

FIN

		puts "Creating #{mdfilename} ..."
		File.open( mdfilename, 'w').puts ym

		mp3.tag.title = title
 		mp3.tag2.COMM = script
	end


end

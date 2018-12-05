from subprocess import Popen, PIPE

#ffmpeg stream command
ffmpeg = ['ffmpeg', '-f', 'alsa', '-i', 'default:CARD=Device'\
		, '-ac', '1', '-hls_time', '1', '-hls_list_size'\
		, '5', '-hls_flags', 'delete_segments', './hls/ronastream.m3u8']

#server command

if __name__ == '__main__':
	f = Popen(ffmpeg, stderr = PIPE, stdout = PIPE)
	print('ffmpeg started')
	
	try:
		f.wait()
	except KeyboardInterrupt:
		print('terminating process')
		f.communicate("q")
		f.wait()

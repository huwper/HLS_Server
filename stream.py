from subprocess import Popen, PIPE, STDOUT
from datetime import datetime

#ffmpeg stream command
ffmpeg = ['ffmpeg', '-f', 'alsa', '-i', 'default:CARD=Device'\
		, '-ac', '1', '-af', 'highpass=f=200', '-af', 'lowpass=f=3000', '-af', 'volume=5'\
		, '-hls_time', '1', '-hls_list_size', '5'\
		, '-hls_flags', 'delete_segments', '/home/pi/repos/HLS_Server/hls/ronastream.m3u8']

#server command

if __name__ == '__main__':
	with open('/home/pi/repos/HLS_Server/log.txt', mode='a') as log:
		log.write('\r\n\r\n>>>>>>>>>> started at {}\r\n'.format(str(datetime.now())))


		f = Popen(ffmpeg, stderr = STDOUT, stdout = PIPE, universal_newlines = True)
	
		try:
			f.wait()
			for line in f.stdout:
				log.write(line)
			log.write('\r\n\r\n>>>>>>>> process finished at {}\r\n'.format(str(datetime.now)))

		except KeyboardInterrupt:
			f.communicate("q")
			f.wait()
			log.write('\r\n\r\n>>>>>>>> process terminated at {}\r\n'.format(str(datetime.now())))

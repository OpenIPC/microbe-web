<%
# line format: parameter|label|units|type|o,p,t,i,o,n,s|placeholder|hint
# line format: parameter|type
mj_retired="
.system.sensorConfigDir|Path to sensors config directory||string||/etc/sensors|
.system.updateChannel|Channel to use for updates||select|testing,beta,stable,none|stable|
.isp.alignWidth|Align width||number||8|
.isp.threadStackSize|Thread stack size|KB|number|1-32|16|
.motionDetect.profile|Motion detection profile||select|outdoor,indoor|outdoor|
.raw.enabled|Enable raw feed support||boolean|true,false|false|
.raw.mode|Raw feed mode||select|slow,fast,none|slow|
"

# line format: parameter|label|units|type|o,p,t,i,o,n,s|placeholder|hint
# number options: min,max,step
# range options: min,max,step[,button]
# select options: value2,value2,value3...
mj="
.system.logLevel|Severity of logging||select|ERROR,WARN,INFO,DEBUG,TRACE|TRACE|Used for syslog messages.
.system.webAdmin|Serve Web Admin via Majestic||boolean|enabled,disabled|disabled|Experimental! Disable on camera with public access.
.system.staticDir|Home directory for static files||string||/var/www/html|
.system.webPort|Port for HTTP access||number|1,65535,1|80|
.system.httpsPort|Port for HTTPS access||number|1,65535,1|443|
.system.httpsCertificate|Path to public SSL certificate||string||/etc/ssl/certs/www.example.com.crt|
.system.httpsCertificateKey|Path to private SSL key||string||/etc/ssl/private/www.example.com.key|
.system.buffer|Maximum buffer size|KB|number||1024|per client
.isp.sensorConfig|Path to sensor configuration file||string||/etc/sensors/imx222_1080p_line.ini|<a href=\"sensor.cgi\">Upload your own driver and config</a>
.isp.memMode|Memory mode||select|normal,reduction|reduction|
.isp.slowShutter|Slow shutter||select|disabled,low,medium,high|low|Automatic frame rate reduction mode.
.isp.antiFlicker|Anti-flicker||select|disabled,50,60|disabled|Usually, the utility frequency in your grid line.
.isp.blkCnt|Block count||number|1,32,1|4|Use 4 for small memory systems, 10+ for performant SoCs.
.isp.exposure|Sensor exposure time|&micro;s|range|1,200,1,auto|auto|From 1 to 200.
.isp.aGain|Sensor analog gain||number|1,10000,1|1|
.isp.dGain|Sensor digital gain||number|1,10000,1|1|
.isp.ispGain|ISP gain||number|1,10000,1|1|
.isp.drc|Dynamic Range Compression (DRC) rate|:1|number|1,1000,1|300|
.isp.lowDelay|Low delay mode||boolean|true,false|false|May break sophisticated settings.
.isp.rawMode|Raw feed mode||select|slow,fast,none|none|
.isp.iqProfile|Path to PQTools binary profile||string|||
.image.mirror|Flip image horizontally||boolean|true,false|false|
.image.flip|Flip image vertically||boolean|true,false|false|
.image.rotate|Rotate image clockwise, °||select|0,90,270|0|
.image.contrast|Image contrast|%|range|1,100,1,auto|auto|
.image.hue|Image hue|%|range|1,100,1|50|
.image.saturation|Image saturation|%|range|1,100,1|50|
.image.luminance|Image luminance|%|range|1,100,1,auto|auto|
.osd.enabled|Enable On-Screen Display (OSD)||boolean|true,false|false|
.osd.font|Path to font file used in OSD||string||/usr/share/fonts/truetype/UbuntuMono-Regular.ttf|
.osd.template|OSD template||string||%a %e %B %Y %H:%M:%S %Z|Supports <a href=\"https://man7.org/linux/man-pages/man3/strftime.3.html \" target=\"_blank\">strftime()</a> format.
.osd.posX|Horizontal position of OSD|px|number|-2000,2000,1|-100|
.osd.posY|Vertical position of OSD|px|number|-2000,2000,1|-100|
.osd.privacyMasks|Privacy masks|px|string||0x0x234x640,2124x0x468x1300|Coordinates of masked areas separated by commas.
.nightMode.enabled|Enable night mode||boolean|true,false|false|
.nightMode.irSensorPin|GPIO pin of signal from IR sensor||number|1,100,1|62|
.nightMode.irSensorPinInvert|IR sensor is inverted||boolean|true,false|false|
.nightMode.irCutPin1|GPIO pin1 of signal for IRcut filter||number|1,100,1|1|
.nightMode.irCutPin2|GPIO pin2 of signal for IRcut filter||number|1,100,1|2|
.nightMode.dncDelay|Delay before toggling Day/Night mode||range|1,60,1|20|
.nightMode.backlightPin|GPIO pin to turn on night mode illumination||number|1,100,1|65|
.nightMode.nightAPI|Use night mode API||boolean|true,false|false|
.nightMode.drcOverride|Dynamic Range Compression (DRC) in night mode||number|1,1000,1|300|
.records.enabled|Enable saving records||boolean|true,false|false|
.records.path|Template for saving video records||string||/mnt/mmc/%Y/%m/%d/%H.mp4|Supports <a href=\"https://man7.org/linux/man-pages/man3/strftime.3.html \" target=\"_blank\">strftime()</a> format.
.records.maxUsage|Limit of available space usage|%|range|1,100,1|95|
.video0.enabled|Enable Video0||boolean|true,false|true|
.video0.codec|Video0 codec||select|h264,h265|h264|
.video0.size|Video resolution|px|string|1920x1080,1280x720,704x576|1920x1080|
.video0.fps|Video frame rate|fps|number|1,60,1|25|
.video0.bitrate|Video bitrate|kbps|number|1,4096,1|4096|
.video0.gopSize|Send I-frames each 1 second||number|0.1,20,0.1|1|
.video0.gopMode|Group of Pictures (GOP) mode||select|normal,dual,smart|normal|
.video0.rcMode|RC mode||select|avbr,cbr,vbr|avbr|
.video0.crop|Crop video to size|px|string||0x0x960x540|
.video0.sliceUnits|Number of slices per frame||number|1,10,1|4
.video1.enabled|Enable Video1||boolean|true,false|false|
.video1.codec|Video1 codec||select|h264,h265|h264|
.video1.size|Video1 resolution|px|string|1920x1080,1280x720,704x576|704x576|
.video1.fps|Video1 frame rate|fps|number|1,60,1|15|
.video1.bitrate|Video1 bitrate|kbps|number|1,4096,1|2048|
.video1.gopSize|Send I-frame each 1 second||number|1,20,1|1|
.video1.gopMode|GOP mode||select|normal,dual,smart|normal|
.video1.rcMode|RC mode||select|avbr|avbr|
.video1.crop|Crop video to size|px|string||0x0x960x540|
.video1.sliceUnits|Number of slices per frame||number|1,10,1|4
.jpeg.enabled|Enable JPEG support||boolean|true,false|true|
.jpeg.size|Snapshot size|px|string||1920x1080|
.jpeg.qfactor|JPEG quality level|%|range|1,100,1|50|
.jpeg.toProgressive|Progressive JPEG||boolean|true,false|false|
.mjpeg.size|Video resolution|px|string||640x360|
.mjpeg.fps|Video framerate|fps|number|1,30,1|5|
.mjpeg.bitrate|Video bitrate|kbps|number|1,4096,1|1024|
.audio.enabled|Enable audio||boolean|true,false|false|
.audio.volume|Audio volume level|%|range|1,100,1,auto|auto|
.audio.srate|Audio sampling rate|kHz|number|1,96000,1|8000|
.audio.codec|Codec for RTSP and MP4 encoding||select|mp3,opus,aac,pcm,alaw,ulaw|opus|
.audio.device|Audio card||string||hw:2|
.audio.outputEnabled|Enable audio output||boolean|true,false|false|
.audio.voiceEqualizer|Audio equalizer||select|disabled,common,music,noisy|disabled|
.rtsp.enabled|Enable output||boolean|true,false|true|
.rtsp.port|Port for RTSP protocol||number|1,65535,1|554|rtsp://${network_address}:[port]/stream={0,1}
.hls.enabled|Enable HTTP Live Streaming (HLS)||boolean|true,false|true|
.youtube.enabled|Enable Youtube support||boolean|true,false|false|
.youtube.key|Youtube API key||string||xxxx-xxxx-xxxx-xxxx-xxxx|
.motionDetect.enabled|Enable motion detection||boolean|true,false|false|
.motionDetect.visualize|Visualize motion detection||boolean|true,false|true|
.motionDetect.debug|Enable debugging||boolean|true,false|true|
.motionDetect.constraints|Regions of Interest (ROI) for motion detection.|px|string||0x0x1296x760|
.ipeye.enabled|Enable IPEYE support||boolean|true,false|false|
.netip.enabled|Enable NETIP protocol support||boolean|true,false|false|
.netip.user|NETIP user||string||admin|
.netip.password-plain|NETIP password||password|||Pain-text password, it will be hashed for NETIP.
.netip.password|NETIP password (hash)||hidden||6V0Y4HLF|
.netip.port|NETIP port||number|1,65535,1|34567|
.netip.snapshots|NETIP snaphots||boolean|true,false|true|
.netip.ignoreSetTime|Ignore set time||boolean|true,false|false|
.onvif.enabled|Enable ONVIF protocol support||boolean|true,false|false|
.watchdog.enabled|Enable watchdog||boolean|true,false|true|
.watchdog.timeout|Watchdog timeout|sec|number|1,600,1|10|
.cloud.enabled|Enable cloud support||boolean|true,false|false|
"

# hide these settings unless in debug mode
mj_params_debug=".isp.aGain .isp.dGain .isp.ispGain"

# conditional settings limiters
mj_show_audio_voiceEqualizer="gk7205v200 hi3516cv300 hi3516cv500 hi3516ev300 hi3519v101"
mj_hide_video0_codec="hi3516cv200 hi3516cv100"
mj_hide_video1_codec="hi3516cv200 hi3516cv100"
mj_hide_motionDetect="hi3516cv100 hi3516av100"
%>

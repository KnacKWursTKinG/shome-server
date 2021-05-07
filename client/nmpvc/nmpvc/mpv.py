

import json
import socket

import requests

from kwking_helper import rq


class MPVBase:
    def __init__(self, host, port = 50870):
        self.url = f"http://{socket.gethostbyname(host)}:{port}/api/nmpv/player"

    def _send_data(self, data):
        resp = requests.post(
            self.url,
            json.loads(data),
            headers={
                'Content-Type': 'application/json'
            }
        )

        if resp.status_code != 200:
            raise rq.RQError(resp)

        return json.loads(resp.text) if "application/json" in resp.headers.get('Content-Type') else None

    def _run_method(self, name: str, *args, **kwargs):
        return self._send_data({
            "attr": str(name),
            "args": args,
            "kwargs": kwargs
        })

    def _set_prop(self, prop: str, value):
        return self._send_data({
            "attr": str(prop),
            "value": value
        })

    def _get_prop(self, prop: str):
        return self._send_data({
            "attr": str(prop)
        })

class MPVProperty(MPVBase):

    @property
    def demuxer_lavf_propagate_opts(self):
        return self._get_prop('demuxer_lavf_propagate_opts')

    @demuxer_lavf_propagate_opts.setter
    def demuxer_lavf_propagate_opts(self, value):
        return self._set_prop('demuxer_lavf_propagate_opts', value)

    @property
    def sub_start(self):
        return self._get_prop('sub_start')

    @sub_start.setter
    def sub_start(self, value):
        return self._set_prop('sub_start', value)

    @property
    def vd_queue_max_samples(self):
        return self._get_prop('vd_queue_max_samples')

    @vd_queue_max_samples.setter
    def vd_queue_max_samples(self, value):
        return self._set_prop('vd_queue_max_samples', value)

    @property
    def cache_secs(self):
        return self._get_prop('cache_secs')

    @cache_secs.setter
    def cache_secs(self, value):
        return self._set_prop('cache_secs', value)

    @property
    def ao_null_channel_layouts(self):
        return self._get_prop('ao_null_channel_layouts')

    @ao_null_channel_layouts.setter
    def ao_null_channel_layouts(self, value):
        return self._set_prop('ao_null_channel_layouts', value)

    @property
    def native_fs(self):
        return self._get_prop('native_fs')

    @native_fs.setter
    def native_fs(self, value):
        return self._set_prop('native_fs', value)

    @property
    def osc(self):
        return self._get_prop('osc')

    @osc.setter
    def osc(self, value):
        return self._set_prop('osc', value)

    @property
    def pulse_allow_suspended(self):
        return self._get_prop('pulse_allow_suspended')

    @pulse_allow_suspended.setter
    def pulse_allow_suspended(self, value):
        return self._set_prop('pulse_allow_suspended', value)

    @property
    def rar_list_all_volumes(self):
        return self._get_prop('rar_list_all_volumes')

    @rar_list_all_volumes.setter
    def rar_list_all_volumes(self, value):
        return self._set_prop('rar_list_all_volumes', value)

    @property
    def demuxer_lavf_buffersize(self):
        return self._get_prop('demuxer_lavf_buffersize')

    @demuxer_lavf_buffersize.setter
    def demuxer_lavf_buffersize(self, value):
        return self._set_prop('demuxer_lavf_buffersize', value)

    @property
    def watch_later_directory(self):
        return self._get_prop('watch_later_directory')

    @watch_later_directory.setter
    def watch_later_directory(self, value):
        return self._set_prop('watch_later_directory', value)

    @property
    def decoder_list(self):
        return self._get_prop('decoder_list')

    @decoder_list.setter
    def decoder_list(self, value):
        return self._set_prop('decoder_list', value)

    @property
    def audio_files(self):
        return self._get_prop('audio_files')

    @audio_files.setter
    def audio_files(self, value):
        return self._set_prop('audio_files', value)

    @property
    def zimg_fast(self):
        return self._get_prop('zimg_fast')

    @zimg_fast.setter
    def zimg_fast(self, value):
        return self._set_prop('zimg_fast', value)

    @property
    def audio_format(self):
        return self._get_prop('audio_format')

    @audio_format.setter
    def audio_format(self, value):
        return self._set_prop('audio_format', value)

    @property
    def demuxer_rawvideo_codec(self):
        return self._get_prop('demuxer_rawvideo_codec')

    @demuxer_rawvideo_codec.setter
    def demuxer_rawvideo_codec(self, value):
        return self._set_prop('demuxer_rawvideo_codec', value)

    @property
    def sub_blur(self):
        return self._get_prop('sub_blur')

    @sub_blur.setter
    def sub_blur(self, value):
        return self._set_prop('sub_blur', value)

    @property
    def tone_mapping_param(self):
        return self._get_prop('tone_mapping_param')

    @tone_mapping_param.setter
    def tone_mapping_param(self, value):
        return self._set_prop('tone_mapping_param', value)

    @property
    def audio_display(self):
        return self._get_prop('audio_display')

    @audio_display.setter
    def audio_display(self, value):
        return self._set_prop('audio_display', value)

    @property
    def audio_bitrate(self):
        return self._get_prop('audio_bitrate')

    @audio_bitrate.setter
    def audio_bitrate(self, value):
        return self._set_prop('audio_bitrate', value)

    @property
    def ovc(self):
        return self._get_prop('ovc')

    @ovc.setter
    def ovc(self, value):
        return self._set_prop('ovc', value)

    @property
    def sub_ass_justify(self):
        return self._get_prop('sub_ass_justify')

    @sub_ass_justify.setter
    def sub_ass_justify(self, value):
        return self._set_prop('sub_ass_justify', value)

    @property
    def sub_use_margins(self):
        return self._get_prop('sub_use_margins')

    @sub_use_margins.setter
    def sub_use_margins(self, value):
        return self._set_prop('sub_use_margins', value)

    @property
    def term_osd_bar(self):
        return self._get_prop('term_osd_bar')

    @term_osd_bar.setter
    def term_osd_bar(self, value):
        return self._set_prop('term_osd_bar', value)

    @property
    def shared_script_properties(self):
        return self._get_prop('shared_script_properties')

    @shared_script_properties.setter
    def shared_script_properties(self, value):
        return self._set_prop('shared_script_properties', value)

    @property
    def sub_text_bold(self):
        return self._get_prop('sub_text_bold')

    @sub_text_bold.setter
    def sub_text_bold(self, value):
        return self._set_prop('sub_text_bold', value)

    @property
    def cdda_sector_size(self):
        return self._get_prop('cdda_sector_size')

    @cdda_sector_size.setter
    def cdda_sector_size(self, value):
        return self._set_prop('cdda_sector_size', value)

    @property
    def cache(self):
        return self._get_prop('cache')

    @cache.setter
    def cache(self, value):
        return self._set_prop('cache', value)

    @property
    def video_align_x(self):
        return self._get_prop('video_align_x')

    @video_align_x.setter
    def video_align_x(self, value):
        return self._set_prop('video_align_x', value)

    @property
    def embeddedfonts(self):
        return self._get_prop('embeddedfonts')

    @embeddedfonts.setter
    def embeddedfonts(self, value):
        return self._set_prop('embeddedfonts', value)

    @property
    def alsa_periods(self):
        return self._get_prop('alsa_periods')

    @alsa_periods.setter
    def alsa_periods(self, value):
        return self._set_prop('alsa_periods', value)

    @property
    def vo_vdpau_sharpen(self):
        return self._get_prop('vo_vdpau_sharpen')

    @vo_vdpau_sharpen.setter
    def vo_vdpau_sharpen(self, value):
        return self._set_prop('vo_vdpau_sharpen', value)

    @property
    def vo_vdpau_queuetime_windowed(self):
        return self._get_prop('vo_vdpau_queuetime_windowed')

    @vo_vdpau_queuetime_windowed.setter
    def vo_vdpau_queuetime_windowed(self, value):
        return self._set_prop('vo_vdpau_queuetime_windowed', value)

    @property
    def osd_justify(self):
        return self._get_prop('osd_justify')

    @osd_justify.setter
    def osd_justify(self, value):
        return self._set_prop('osd_justify', value)

    @property
    def force_rgba_osd_rendering(self):
        return self._get_prop('force_rgba_osd_rendering')

    @force_rgba_osd_rendering.setter
    def force_rgba_osd_rendering(self, value):
        return self._set_prop('force_rgba_osd_rendering', value)

    @property
    def autoload_files(self):
        return self._get_prop('autoload_files')

    @autoload_files.setter
    def autoload_files(self, value):
        return self._set_prop('autoload_files', value)

    @property
    def chapters(self):
        return self._get_prop('chapters')

    @chapters.setter
    def chapters(self, value):
        return self._set_prop('chapters', value)

    @property
    def cursor_autohide(self):
        return self._get_prop('cursor_autohide')

    @cursor_autohide.setter
    def cursor_autohide(self, value):
        return self._set_prop('cursor_autohide', value)

    @property
    def dump_stats(self):
        return self._get_prop('dump_stats')

    @dump_stats.setter
    def dump_stats(self, value):
        return self._set_prop('dump_stats', value)

    @property
    def sharpen(self):
        return self._get_prop('sharpen')

    @sharpen.setter
    def sharpen(self, value):
        return self._set_prop('sharpen', value)

    @property
    def video_align_y(self):
        return self._get_prop('video_align_y')

    @video_align_y.setter
    def video_align_y(self, value):
        return self._set_prop('video_align_y', value)

    @property
    def vo_vdpau_force_yuv(self):
        return self._get_prop('vo_vdpau_force_yuv')

    @vo_vdpau_force_yuv.setter
    def vo_vdpau_force_yuv(self, value):
        return self._set_prop('vo_vdpau_force_yuv', value)

    @property
    def window_maximized(self):
        return self._get_prop('window_maximized')

    @window_maximized.setter
    def window_maximized(self, value):
        return self._set_prop('window_maximized', value)

    @property
    def stream_path(self):
        return self._get_prop('stream_path')

    @stream_path.setter
    def stream_path(self, value):
        return self._set_prop('stream_path', value)

    @property
    def x11_name(self):
        return self._get_prop('x11_name')

    @x11_name.setter
    def x11_name(self, value):
        return self._set_prop('x11_name', value)

    @property
    def partially_seekable(self):
        return self._get_prop('partially_seekable')

    @partially_seekable.setter
    def partially_seekable(self, value):
        return self._set_prop('partially_seekable', value)

    @property
    def height(self):
        return self._get_prop('height')

    @height.setter
    def height(self, value):
        return self._set_prop('height', value)

    @property
    def sub_demuxer(self):
        return self._get_prop('sub_demuxer')

    @sub_demuxer.setter
    def sub_demuxer(self, value):
        return self._set_prop('sub_demuxer', value)

    @property
    def xv_adaptor(self):
        return self._get_prop('xv_adaptor')

    @xv_adaptor.setter
    def xv_adaptor(self, value):
        return self._set_prop('xv_adaptor', value)

    @property
    def audio_backward_overlap(self):
        return self._get_prop('audio_backward_overlap')

    @audio_backward_overlap.setter
    def audio_backward_overlap(self, value):
        return self._set_prop('audio_backward_overlap', value)

    @property
    def demuxer_cache_wait(self):
        return self._get_prop('demuxer_cache_wait')

    @demuxer_cache_wait.setter
    def demuxer_cache_wait(self, value):
        return self._set_prop('demuxer_cache_wait', value)

    @property
    def time_remaining(self):
        return self._get_prop('time_remaining')

    @time_remaining.setter
    def time_remaining(self, value):
        return self._set_prop('time_remaining', value)

    @property
    def vo_null_fps(self):
        return self._get_prop('vo_null_fps')

    @vo_null_fps.setter
    def vo_null_fps(self, value):
        return self._set_prop('vo_null_fps', value)

    @property
    def vaapi_device(self):
        return self._get_prop('vaapi_device')

    @vaapi_device.setter
    def vaapi_device(self, value):
        return self._set_prop('vaapi_device', value)

    @property
    def autosync(self):
        return self._get_prop('autosync')

    @autosync.setter
    def autosync(self, value):
        return self._set_prop('autosync', value)

    @property
    def vd_lavc_check_hw_profile(self):
        return self._get_prop('vd_lavc_check_hw_profile')

    @vd_lavc_check_hw_profile.setter
    def vd_lavc_check_hw_profile(self, value):
        return self._set_prop('vd_lavc_check_hw_profile', value)

    @property
    def gpu_tex_pad_y(self):
        return self._get_prop('gpu_tex_pad_y')

    @gpu_tex_pad_y.setter
    def gpu_tex_pad_y(self, value):
        return self._set_prop('gpu_tex_pad_y', value)

    @property
    def osd_width(self):
        return self._get_prop('osd_width')

    @osd_width.setter
    def osd_width(self, value):
        return self._set_prop('osd_width', value)

    @property
    def demuxer_rawaudio_channels(self):
        return self._get_prop('demuxer_rawaudio_channels')

    @demuxer_rawaudio_channels.setter
    def demuxer_rawaudio_channels(self, value):
        return self._set_prop('demuxer_rawaudio_channels', value)

    @property
    def sub_text_back_color(self):
        return self._get_prop('sub_text_back_color')

    @sub_text_back_color.setter
    def sub_text_back_color(self, value):
        return self._set_prop('sub_text_back_color', value)

    @property
    def window_dragging(self):
        return self._get_prop('window_dragging')

    @window_dragging.setter
    def window_dragging(self, value):
        return self._set_prop('window_dragging', value)

    @property
    def video_rotate(self):
        return self._get_prop('video_rotate')

    @video_rotate.setter
    def video_rotate(self, value):
        return self._set_prop('video_rotate', value)

    @property
    def alsa_buffer_time(self):
        return self._get_prop('alsa_buffer_time')

    @alsa_buffer_time.setter
    def alsa_buffer_time(self, value):
        return self._set_prop('alsa_buffer_time', value)

    @property
    def sub_border_color(self):
        return self._get_prop('sub_border_color')

    @sub_border_color.setter
    def sub_border_color(self, value):
        return self._set_prop('sub_border_color', value)

    @property
    def sub_filter_sdh(self):
        return self._get_prop('sub_filter_sdh')

    @sub_filter_sdh.setter
    def sub_filter_sdh(self, value):
        return self._set_prop('sub_filter_sdh', value)

    @property
    def playlist_count(self):
        return self._get_prop('playlist_count')

    @playlist_count.setter
    def playlist_count(self, value):
        return self._set_prop('playlist_count', value)

    @property
    def keep_open_pause(self):
        return self._get_prop('keep_open_pause')

    @keep_open_pause.setter
    def keep_open_pause(self, value):
        return self._set_prop('keep_open_pause', value)

    @property
    def ofopts(self):
        return self._get_prop('ofopts')

    @ofopts.setter
    def ofopts(self, value):
        return self._set_prop('ofopts', value)

    @property
    def playlist_filenames(self):
        return self._get_prop('playlist_filenames')

    @playlist_filenames.setter
    def playlist_filenames(self, value):
        return self._set_prop('playlist_filenames', value)

    @property
    def cscale_blur(self):
        return self._get_prop('cscale_blur')

    @cscale_blur.setter
    def cscale_blur(self, value):
        return self._set_prop('cscale_blur', value)

    @property
    def ao(self):
        return self._get_prop('ao')

    @ao.setter
    def ao(self, value):
        return self._set_prop('ao', value)

    @property
    def ad_lavc_downmix(self):
        return self._get_prop('ad_lavc_downmix')

    @ad_lavc_downmix.setter
    def ad_lavc_downmix(self, value):
        return self._set_prop('ad_lavc_downmix', value)

    @property
    def load_scripts(self):
        return self._get_prop('load_scripts')

    @load_scripts.setter
    def load_scripts(self, value):
        return self._set_prop('load_scripts', value)

    @property
    def user_agent(self):
        return self._get_prop('user_agent')

    @user_agent.setter
    def user_agent(self, value):
        return self._set_prop('user_agent', value)

    @property
    def ao_null_broken_eof(self):
        return self._get_prop('ao_null_broken_eof')

    @ao_null_broken_eof.setter
    def ao_null_broken_eof(self, value):
        return self._set_prop('ao_null_broken_eof', value)

    @property
    def osd_spacing(self):
        return self._get_prop('osd_spacing')

    @osd_spacing.setter
    def osd_spacing(self, value):
        return self._set_prop('osd_spacing', value)

    @property
    def sub_text_align_y(self):
        return self._get_prop('sub_text_align_y')

    @sub_text_align_y.setter
    def sub_text_align_y(self, value):
        return self._set_prop('sub_text_align_y', value)

    @property
    def write_filename_in_watch_later_config(self):
        return self._get_prop('write_filename_in_watch_later_config')

    @write_filename_in_watch_later_config.setter
    def write_filename_in_watch_later_config(self, value):
        return self._set_prop('write_filename_in_watch_later_config', value)

    @property
    def dscale_taper(self):
        return self._get_prop('dscale_taper')

    @dscale_taper.setter
    def dscale_taper(self, value):
        return self._set_prop('dscale_taper', value)

    @property
    def vf_defaults(self):
        return self._get_prop('vf_defaults')

    @vf_defaults.setter
    def vf_defaults(self, value):
        return self._set_prop('vf_defaults', value)

    @property
    def video_margin_ratio_right(self):
        return self._get_prop('video_margin_ratio_right')

    @video_margin_ratio_right.setter
    def video_margin_ratio_right(self, value):
        return self._set_prop('video_margin_ratio_right', value)

    @property
    def alsa_non_interleaved(self):
        return self._get_prop('alsa_non_interleaved')

    @alsa_non_interleaved.setter
    def alsa_non_interleaved(self, value):
        return self._set_prop('alsa_non_interleaved', value)

    @property
    def vd_queue_enable(self):
        return self._get_prop('vd_queue_enable')

    @vd_queue_enable.setter
    def vd_queue_enable(self, value):
        return self._set_prop('vd_queue_enable', value)

    @property
    def demuxer(self):
        return self._get_prop('demuxer')

    @demuxer.setter
    def demuxer(self, value):
        return self._set_prop('demuxer', value)

    @property
    def opengl_tex_pad_x(self):
        return self._get_prop('opengl_tex_pad_x')

    @opengl_tex_pad_x.setter
    def opengl_tex_pad_x(self, value):
        return self._set_prop('opengl_tex_pad_x', value)

    @property
    def osd_margin_x(self):
        return self._get_prop('osd_margin_x')

    @osd_margin_x.setter
    def osd_margin_x(self, value):
        return self._set_prop('osd_margin_x', value)

    @property
    def properties(self):
        return self._get_prop('properties')

    @properties.setter
    def properties(self, value):
        return self._set_prop('properties', value)

    @property
    def track_auto_selection(self):
        return self._get_prop('track_auto_selection')

    @track_auto_selection.setter
    def track_auto_selection(self, value):
        return self._set_prop('track_auto_selection', value)

    @property
    def scale_param2(self):
        return self._get_prop('scale_param2')

    @scale_param2.setter
    def scale_param2(self, value):
        return self._set_prop('scale_param2', value)

    @property
    def ass_use_margins(self):
        return self._get_prop('ass_use_margins')

    @ass_use_margins.setter
    def ass_use_margins(self, value):
        return self._set_prop('ass_use_margins', value)

    @property
    def demuxer_max_bytes(self):
        return self._get_prop('demuxer_max_bytes')

    @demuxer_max_bytes.setter
    def demuxer_max_bytes(self, value):
        return self._set_prop('demuxer_max_bytes', value)

    @property
    def scale_radius(self):
        return self._get_prop('scale_radius')

    @scale_radius.setter
    def scale_radius(self, value):
        return self._set_prop('scale_radius', value)

    @property
    def tscale_taper(self):
        return self._get_prop('tscale_taper')

    @tscale_taper.setter
    def tscale_taper(self, value):
        return self._set_prop('tscale_taper', value)

    @property
    def hdr_scene_threshold_high(self):
        return self._get_prop('hdr_scene_threshold_high')

    @hdr_scene_threshold_high.setter
    def hdr_scene_threshold_high(self, value):
        return self._set_prop('hdr_scene_threshold_high', value)

    @property
    def file_local(self):
        return self._get_prop('file_local')

    @file_local.setter
    def file_local(self, value):
        return self._set_prop('file_local', value)

    @property
    def sws_allow_zimg(self):
        return self._get_prop('sws_allow_zimg')

    @sws_allow_zimg.setter
    def sws_allow_zimg(self, value):
        return self._set_prop('sws_allow_zimg', value)

    @property
    def audio_stream_silence(self):
        return self._get_prop('audio_stream_silence')

    @audio_stream_silence.setter
    def audio_stream_silence(self, value):
        return self._set_prop('audio_stream_silence', value)

    @property
    def vulkan_async_transfer(self):
        return self._get_prop('vulkan_async_transfer')

    @vulkan_async_transfer.setter
    def vulkan_async_transfer(self, value):
        return self._set_prop('vulkan_async_transfer', value)

    @property
    def ytdl(self):
        return self._get_prop('ytdl')

    @ytdl.setter
    def ytdl(self, value):
        return self._set_prop('ytdl', value)

    @property
    def sub_scale_with_window(self):
        return self._get_prop('sub_scale_with_window')

    @sub_scale_with_window.setter
    def sub_scale_with_window(self, value):
        return self._set_prop('sub_scale_with_window', value)

    @property
    def ad(self):
        return self._get_prop('ad')

    @ad.setter
    def ad(self, value):
        return self._set_prop('ad', value)

    @property
    def opengl_pbo(self):
        return self._get_prop('opengl_pbo')

    @opengl_pbo.setter
    def opengl_pbo(self, value):
        return self._set_prop('opengl_pbo', value)

    @property
    def playing_msg(self):
        return self._get_prop('playing_msg')

    @playing_msg.setter
    def playing_msg(self, value):
        return self._set_prop('playing_msg', value)

    @property
    def sws_cs(self):
        return self._get_prop('sws_cs')

    @sws_cs.setter
    def sws_cs(self, value):
        return self._set_prop('sws_cs', value)

    @property
    def tls_verify(self):
        return self._get_prop('tls_verify')

    @tls_verify.setter
    def tls_verify(self, value):
        return self._set_prop('tls_verify', value)

    @property
    def ontop_level(self):
        return self._get_prop('ontop_level')

    @ontop_level.setter
    def ontop_level(self, value):
        return self._set_prop('ontop_level', value)

    @property
    def path(self):
        return self._get_prop('path')

    @path.setter
    def path(self, value):
        return self._set_prop('path', value)

    @property
    def stream_buffer_size(self):
        return self._get_prop('stream_buffer_size')

    @stream_buffer_size.setter
    def stream_buffer_size(self, value):
        return self._set_prop('stream_buffer_size', value)

    @property
    def hwdec_extra_frames(self):
        return self._get_prop('hwdec_extra_frames')

    @hwdec_extra_frames.setter
    def hwdec_extra_frames(self, value):
        return self._set_prop('hwdec_extra_frames', value)

    @property
    def cache_pause_wait(self):
        return self._get_prop('cache_pause_wait')

    @cache_pause_wait.setter
    def cache_pause_wait(self, value):
        return self._set_prop('cache_pause_wait', value)

    @property
    def ass_hinting(self):
        return self._get_prop('ass_hinting')

    @ass_hinting.setter
    def ass_hinting(self, value):
        return self._set_prop('ass_hinting', value)

    @property
    def demuxer_lavf_analyzeduration(self):
        return self._get_prop('demuxer_lavf_analyzeduration')

    @demuxer_lavf_analyzeduration.setter
    def demuxer_lavf_analyzeduration(self, value):
        return self._set_prop('demuxer_lavf_analyzeduration', value)

    @property
    def filtered_metadata(self):
        return self._get_prop('filtered_metadata')

    @filtered_metadata.setter
    def filtered_metadata(self, value):
        return self._set_prop('filtered_metadata', value)

    @property
    def cscale_taper(self):
        return self._get_prop('cscale_taper')

    @cscale_taper.setter
    def cscale_taper(self, value):
        return self._set_prop('cscale_taper', value)

    @property
    def scale(self):
        return self._get_prop('scale')

    @scale.setter
    def scale(self, value):
        return self._set_prop('scale', value)

    @property
    def lua_opts(self):
        return self._get_prop('lua_opts')

    @lua_opts.setter
    def lua_opts(self, value):
        return self._set_prop('lua_opts', value)

    @property
    def demuxer_via_network(self):
        return self._get_prop('demuxer_via_network')

    @demuxer_via_network.setter
    def demuxer_via_network(self, value):
        return self._set_prop('demuxer_via_network', value)

    @property
    def gpu_tex_pad_x(self):
        return self._get_prop('gpu_tex_pad_x')

    @gpu_tex_pad_x.setter
    def gpu_tex_pad_x(self, value):
        return self._set_prop('gpu_tex_pad_x', value)

    @property
    def slang(self):
        return self._get_prop('slang')

    @slang.setter
    def slang(self, value):
        return self._set_prop('slang', value)

    @property
    def ass_style_override(self):
        return self._get_prop('ass_style_override')

    @ass_style_override.setter
    def ass_style_override(self, value):
        return self._set_prop('ass_style_override', value)

    @property
    def cache_on_disk(self):
        return self._get_prop('cache_on_disk')

    @cache_on_disk.setter
    def cache_on_disk(self, value):
        return self._set_prop('cache_on_disk', value)

    @property
    def decoder_frame_drop_count(self):
        return self._get_prop('decoder_frame_drop_count')

    @decoder_frame_drop_count.setter
    def decoder_frame_drop_count(self, value):
        return self._set_prop('decoder_frame_drop_count', value)

    @property
    def sub_filter_regex(self):
        return self._get_prop('sub_filter_regex')

    @sub_filter_regex.setter
    def sub_filter_regex(self, value):
        return self._set_prop('sub_filter_regex', value)

    @property
    def vd_lavc_framedrop(self):
        return self._get_prop('vd_lavc_framedrop')

    @vd_lavc_framedrop.setter
    def vd_lavc_framedrop(self, value):
        return self._set_prop('vd_lavc_framedrop', value)

    @property
    def zimg_dither(self):
        return self._get_prop('zimg_dither')

    @zimg_dither.setter
    def zimg_dither(self, value):
        return self._set_prop('zimg_dither', value)

    @property
    def volume_max(self):
        return self._get_prop('volume_max')

    @volume_max.setter
    def volume_max(self, value):
        return self._set_prop('volume_max', value)

    @property
    def ad_queue_max_bytes(self):
        return self._get_prop('ad_queue_max_bytes')

    @ad_queue_max_bytes.setter
    def ad_queue_max_bytes(self, value):
        return self._set_prop('ad_queue_max_bytes', value)

    @property
    def audio_pts(self):
        return self._get_prop('audio_pts')

    @audio_pts.setter
    def audio_pts(self, value):
        return self._set_prop('audio_pts', value)

    @property
    def on_all_workspaces(self):
        return self._get_prop('on_all_workspaces')

    @on_all_workspaces.setter
    def on_all_workspaces(self, value):
        return self._set_prop('on_all_workspaces', value)

    @property
    def sub_ass_style_override(self):
        return self._get_prop('sub_ass_style_override')

    @sub_ass_style_override.setter
    def sub_ass_style_override(self, value):
        return self._set_prop('sub_ass_style_override', value)

    @property
    def stretch_image_subs_to_screen(self):
        return self._get_prop('stretch_image_subs_to_screen')

    @stretch_image_subs_to_screen.setter
    def stretch_image_subs_to_screen(self, value):
        return self._set_prop('stretch_image_subs_to_screen', value)

    @property
    def sub_text_border_color(self):
        return self._get_prop('sub_text_border_color')

    @sub_text_border_color.setter
    def sub_text_border_color(self, value):
        return self._set_prop('sub_text_border_color', value)

    @property
    def tls_ca_file(self):
        return self._get_prop('tls_ca_file')

    @tls_ca_file.setter
    def tls_ca_file(self, value):
        return self._set_prop('tls_ca_file', value)

    @property
    def ovoffset(self):
        return self._get_prop('ovoffset')

    @ovoffset.setter
    def ovoffset(self, value):
        return self._set_prop('ovoffset', value)

    @property
    def dscale_cutoff(self):
        return self._get_prop('dscale_cutoff')

    @dscale_cutoff.setter
    def dscale_cutoff(self, value):
        return self._set_prop('dscale_cutoff', value)

    @property
    def vlang(self):
        return self._get_prop('vlang')

    @vlang.setter
    def vlang(self, value):
        return self._set_prop('vlang', value)

    @property
    def xv_colorkey(self):
        return self._get_prop('xv_colorkey')

    @xv_colorkey.setter
    def xv_colorkey(self, value):
        return self._set_prop('xv_colorkey', value)

    @property
    def window_minimized(self):
        return self._get_prop('window_minimized')

    @window_minimized.setter
    def window_minimized(self, value):
        return self._set_prop('window_minimized', value)

    @property
    def tls_cert_file(self):
        return self._get_prop('tls_cert_file')

    @tls_cert_file.setter
    def tls_cert_file(self, value):
        return self._set_prop('tls_cert_file', value)

    @property
    def hwdec_image_format(self):
        return self._get_prop('hwdec_image_format')

    @hwdec_image_format.setter
    def hwdec_image_format(self, value):
        return self._set_prop('hwdec_image_format', value)

    @property
    def alsa_mixer_index(self):
        return self._get_prop('alsa_mixer_index')

    @alsa_mixer_index.setter
    def alsa_mixer_index(self, value):
        return self._set_prop('alsa_mixer_index', value)

    @property
    def input_media_keys(self):
        return self._get_prop('input_media_keys')

    @input_media_keys.setter
    def input_media_keys(self, value):
        return self._set_prop('input_media_keys', value)

    @property
    def sub_bitrate(self):
        return self._get_prop('sub_bitrate')

    @sub_bitrate.setter
    def sub_bitrate(self, value):
        return self._set_prop('sub_bitrate', value)

    @property
    def gpu_dumb_mode(self):
        return self._get_prop('gpu_dumb_mode')

    @gpu_dumb_mode.setter
    def gpu_dumb_mode(self, value):
        return self._set_prop('gpu_dumb_mode', value)

    @property
    def sub_create_cc_track(self):
        return self._get_prop('sub_create_cc_track')

    @sub_create_cc_track.setter
    def sub_create_cc_track(self, value):
        return self._set_prop('sub_create_cc_track', value)

    @property
    def hr_seek_framedrop(self):
        return self._get_prop('hr_seek_framedrop')

    @hr_seek_framedrop.setter
    def hr_seek_framedrop(self, value):
        return self._set_prop('hr_seek_framedrop', value)

    @property
    def dvdangle(self):
        return self._get_prop('dvdangle')

    @dvdangle.setter
    def dvdangle(self, value):
        return self._set_prop('dvdangle', value)

    @property
    def sub_ass_force_style(self):
        return self._get_prop('sub_ass_force_style')

    @sub_ass_force_style.setter
    def sub_ass_force_style(self, value):
        return self._set_prop('sub_ass_force_style', value)

    @property
    def msgmodule(self):
        return self._get_prop('msgmodule')

    @msgmodule.setter
    def msgmodule(self, value):
        return self._set_prop('msgmodule', value)

    @property
    def demuxer_mkv_probe_start_time(self):
        return self._get_prop('demuxer_mkv_probe_start_time')

    @demuxer_mkv_probe_start_time.setter
    def demuxer_mkv_probe_start_time(self, value):
        return self._set_prop('demuxer_mkv_probe_start_time', value)

    @property
    def scale_cutoff(self):
        return self._get_prop('scale_cutoff')

    @scale_cutoff.setter
    def scale_cutoff(self, value):
        return self._set_prop('scale_cutoff', value)

    @property
    def demuxer_rawvideo_format(self):
        return self._get_prop('demuxer_rawvideo_format')

    @demuxer_rawvideo_format.setter
    def demuxer_rawvideo_format(self, value):
        return self._set_prop('demuxer_rawvideo_format', value)

    @property
    def video_frame_info(self):
        return self._get_prop('video_frame_info')

    @video_frame_info.setter
    def video_frame_info(self, value):
        return self._set_prop('video_frame_info', value)

    @property
    def mouse_pos(self):
        return self._get_prop('mouse_pos')

    @mouse_pos.setter
    def mouse_pos(self, value):
        return self._set_prop('mouse_pos', value)

    @property
    def ao_pcm_waveheader(self):
        return self._get_prop('ao_pcm_waveheader')

    @ao_pcm_waveheader.setter
    def ao_pcm_waveheader(self, value):
        return self._set_prop('ao_pcm_waveheader', value)

    @property
    def ab_loop_b(self):
        return self._get_prop('ab_loop_b')

    @ab_loop_b.setter
    def ab_loop_b(self, value):
        return self._set_prop('ab_loop_b', value)

    @property
    def cdda_paranoia(self):
        return self._get_prop('cdda_paranoia')

    @cdda_paranoia.setter
    def cdda_paranoia(self, value):
        return self._set_prop('cdda_paranoia', value)

    @property
    def correct_downscaling(self):
        return self._get_prop('correct_downscaling')

    @correct_downscaling.setter
    def correct_downscaling(self, value):
        return self._set_prop('correct_downscaling', value)

    @property
    def ab_loop_a(self):
        return self._get_prop('ab_loop_a')

    @ab_loop_a.setter
    def ab_loop_a(self, value):
        return self._set_prop('ab_loop_a', value)

    @property
    def replaygain(self):
        return self._get_prop('replaygain')

    @replaygain.setter
    def replaygain(self, value):
        return self._set_prop('replaygain', value)

    @property
    def container_fps(self):
        return self._get_prop('container_fps')

    @container_fps.setter
    def container_fps(self, value):
        return self._set_prop('container_fps', value)

    @property
    def icc_profile(self):
        return self._get_prop('icc_profile')

    @icc_profile.setter
    def icc_profile(self, value):
        return self._set_prop('icc_profile', value)

    @property
    def percent_pos(self):
        return self._get_prop('percent_pos')

    @percent_pos.setter
    def percent_pos(self, value):
        return self._set_prop('percent_pos', value)

    @property
    def audio_client_name(self):
        return self._get_prop('audio_client_name')

    @audio_client_name.setter
    def audio_client_name(self, value):
        return self._set_prop('audio_client_name', value)

    @property
    def cursor_autohide_delay(self):
        return self._get_prop('cursor_autohide_delay')

    @cursor_autohide_delay.setter
    def cursor_autohide_delay(self, value):
        return self._set_prop('cursor_autohide_delay', value)

    @property
    def video(self):
        return self._get_prop('video')

    @video.setter
    def video(self, value):
        return self._set_prop('video', value)

    @property
    def jack_port(self):
        return self._get_prop('jack_port')

    @jack_port.setter
    def jack_port(self, value):
        return self._set_prop('jack_port', value)

    @property
    def fbo_format(self):
        return self._get_prop('fbo_format')

    @fbo_format.setter
    def fbo_format(self, value):
        return self._set_prop('fbo_format', value)

    @property
    def tscale_cutoff(self):
        return self._get_prop('tscale_cutoff')

    @tscale_cutoff.setter
    def tscale_cutoff(self, value):
        return self._set_prop('tscale_cutoff', value)

    @property
    def fullscreen(self):
        return self._get_prop('fullscreen')

    @fullscreen.setter
    def fullscreen(self, value):
        return self._set_prop('fullscreen', value)

    @property
    def xv_buffers(self):
        return self._get_prop('xv_buffers')

    @xv_buffers.setter
    def xv_buffers(self, value):
        return self._set_prop('xv_buffers', value)

    @property
    def sub_ass(self):
        return self._get_prop('sub_ass')

    @sub_ass.setter
    def sub_ass(self, value):
        return self._set_prop('sub_ass', value)

    @property
    def video_bitrate(self):
        return self._get_prop('video_bitrate')

    @video_bitrate.setter
    def video_bitrate(self, value):
        return self._set_prop('video_bitrate', value)

    @property
    def hdr_scene_threshold_low(self):
        return self._get_prop('hdr_scene_threshold_low')

    @hdr_scene_threshold_low.setter
    def hdr_scene_threshold_low(self, value):
        return self._set_prop('hdr_scene_threshold_low', value)

    @property
    def osd_back_color(self):
        return self._get_prop('osd_back_color')

    @osd_back_color.setter
    def osd_back_color(self, value):
        return self._set_prop('osd_back_color', value)

    @property
    def vo_vdpau_output_surfaces(self):
        return self._get_prop('vo_vdpau_output_surfaces')

    @vo_vdpau_output_surfaces.setter
    def vo_vdpau_output_surfaces(self, value):
        return self._set_prop('vo_vdpau_output_surfaces', value)

    @property
    def msg_time(self):
        return self._get_prop('msg_time')

    @msg_time.setter
    def msg_time(self, value):
        return self._set_prop('msg_time', value)

    @property
    def sws_fast(self):
        return self._get_prop('sws_fast')

    @sws_fast.setter
    def sws_fast(self, value):
        return self._set_prop('sws_fast', value)

    @property
    def oac(self):
        return self._get_prop('oac')

    @oac.setter
    def oac(self, value):
        return self._set_prop('oac', value)

    @property
    def mpv_configuration(self):
        return self._get_prop('mpv_configuration')

    @mpv_configuration.setter
    def mpv_configuration(self, value):
        return self._set_prop('mpv_configuration', value)

    @property
    def image_display_duration(self):
        return self._get_prop('image_display_duration')

    @image_display_duration.setter
    def image_display_duration(self, value):
        return self._set_prop('image_display_duration', value)

    @property
    def sub_bold(self):
        return self._get_prop('sub_bold')

    @sub_bold.setter
    def sub_bold(self, value):
        return self._set_prop('sub_bold', value)

    @property
    def ao_pcm_file(self):
        return self._get_prop('ao_pcm_file')

    @ao_pcm_file.setter
    def ao_pcm_file(self, value):
        return self._set_prop('ao_pcm_file', value)

    @property
    def sub_shadow_offset(self):
        return self._get_prop('sub_shadow_offset')

    @sub_shadow_offset.setter
    def sub_shadow_offset(self, value):
        return self._set_prop('sub_shadow_offset', value)

    @property
    def opengl_es(self):
        return self._get_prop('opengl_es')

    @opengl_es.setter
    def opengl_es(self, value):
        return self._set_prop('opengl_es', value)

    @property
    def audio_codec(self):
        return self._get_prop('audio_codec')

    @audio_codec.setter
    def audio_codec(self, value):
        return self._set_prop('audio_codec', value)

    @property
    def prefetch_playlist(self):
        return self._get_prop('prefetch_playlist')

    @prefetch_playlist.setter
    def prefetch_playlist(self, value):
        return self._set_prop('prefetch_playlist', value)

    @property
    def use_filedir_conf(self):
        return self._get_prop('use_filedir_conf')

    @use_filedir_conf.setter
    def use_filedir_conf(self, value):
        return self._set_prop('use_filedir_conf', value)

    @property
    def video_reversal_buffer(self):
        return self._get_prop('video_reversal_buffer')

    @video_reversal_buffer.setter
    def video_reversal_buffer(self, value):
        return self._set_prop('video_reversal_buffer', value)

    @property
    def width(self):
        return self._get_prop('width')

    @width.setter
    def width(self, value):
        return self._set_prop('width', value)

    @property
    def deband_iterations(self):
        return self._get_prop('deband_iterations')

    @deband_iterations.setter
    def deband_iterations(self, value):
        return self._set_prop('deband_iterations', value)

    @property
    def metadata(self):
        return self._get_prop('metadata')

    @metadata.setter
    def metadata(self, value):
        return self._set_prop('metadata', value)

    @property
    def audio_resample_filter_size(self):
        return self._get_prop('audio_resample_filter_size')

    @audio_resample_filter_size.setter
    def audio_resample_filter_size(self, value):
        return self._set_prop('audio_resample_filter_size', value)

    @property
    def audio_fallback_to_null(self):
        return self._get_prop('audio_fallback_to_null')

    @audio_fallback_to_null.setter
    def audio_fallback_to_null(self, value):
        return self._set_prop('audio_fallback_to_null', value)

    @property
    def osd_border_color(self):
        return self._get_prop('osd_border_color')

    @osd_border_color.setter
    def osd_border_color(self, value):
        return self._set_prop('osd_border_color', value)

    @property
    def vo_image_png_filter(self):
        return self._get_prop('vo_image_png_filter')

    @vo_image_png_filter.setter
    def vo_image_png_filter(self, value):
        return self._set_prop('vo_image_png_filter', value)

    @property
    def demuxer_donate_buffer(self):
        return self._get_prop('demuxer_donate_buffer')

    @demuxer_donate_buffer.setter
    def demuxer_donate_buffer(self, value):
        return self._set_prop('demuxer_donate_buffer', value)

    @property
    def audio_swresample_o(self):
        return self._get_prop('audio_swresample_o')

    @audio_swresample_o.setter
    def audio_swresample_o(self, value):
        return self._set_prop('audio_swresample_o', value)

    @property
    def index(self):
        return self._get_prop('index')

    @index.setter
    def index(self, value):
        return self._set_prop('index', value)

    @property
    def cscale_radius(self):
        return self._get_prop('cscale_radius')

    @cscale_radius.setter
    def cscale_radius(self, value):
        return self._set_prop('cscale_radius', value)

    @property
    def sub_speed(self):
        return self._get_prop('sub_speed')

    @sub_speed.setter
    def sub_speed(self, value):
        return self._set_prop('sub_speed', value)

    @property
    def vulkan_disable_events(self):
        return self._get_prop('vulkan_disable_events')

    @vulkan_disable_events.setter
    def vulkan_disable_events(self, value):
        return self._set_prop('vulkan_disable_events', value)

    @property
    def sub_forced_only(self):
        return self._get_prop('sub_forced_only')

    @sub_forced_only.setter
    def sub_forced_only(self, value):
        return self._set_prop('sub_forced_only', value)

    @property
    def video_latency_hacks(self):
        return self._get_prop('video_latency_hacks')

    @video_latency_hacks.setter
    def video_latency_hacks(self, value):
        return self._set_prop('video_latency_hacks', value)

    @property
    def fs_screen(self):
        return self._get_prop('fs_screen')

    @fs_screen.setter
    def fs_screen(self, value):
        return self._set_prop('fs_screen', value)

    @property
    def af_defaults(self):
        return self._get_prop('af_defaults')

    @af_defaults.setter
    def af_defaults(self, value):
        return self._set_prop('af_defaults', value)

    @property
    def deband_threshold(self):
        return self._get_prop('deband_threshold')

    @deband_threshold.setter
    def deband_threshold(self, value):
        return self._set_prop('deband_threshold', value)

    @property
    def demuxer_rawvideo_mp_format(self):
        return self._get_prop('demuxer_rawvideo_mp_format')

    @demuxer_rawvideo_mp_format.setter
    def demuxer_rawvideo_mp_format(self, value):
        return self._set_prop('demuxer_rawvideo_mp_format', value)

    @property
    def scale_wblur(self):
        return self._get_prop('scale_wblur')

    @scale_wblur.setter
    def scale_wblur(self, value):
        return self._set_prop('scale_wblur', value)

    @property
    def target_trc(self):
        return self._get_prop('target_trc')

    @target_trc.setter
    def target_trc(self, value):
        return self._set_prop('target_trc', value)

    @property
    def current_ao(self):
        return self._get_prop('current_ao')

    @current_ao.setter
    def current_ao(self, value):
        return self._set_prop('current_ao', value)

    @property
    def handle(self):
        return self._get_prop('handle')

    @handle.setter
    def handle(self, value):
        return self._set_prop('handle', value)

    @property
    def icc_contrast(self):
        return self._get_prop('icc_contrast')

    @icc_contrast.setter
    def icc_contrast(self, value):
        return self._set_prop('icc_contrast', value)

    @property
    def sub_files(self):
        return self._get_prop('sub_files')

    @sub_files.setter
    def sub_files(self, value):
        return self._set_prop('sub_files', value)

    @property
    def audio_resample_linear(self):
        return self._get_prop('audio_resample_linear')

    @audio_resample_linear.setter
    def audio_resample_linear(self, value):
        return self._set_prop('audio_resample_linear', value)

    @property
    def play_dir(self):
        return self._get_prop('play_dir')

    @play_dir.setter
    def play_dir(self, value):
        return self._set_prop('play_dir', value)

    @property
    def chapter(self):
        return self._get_prop('chapter')

    @chapter.setter
    def chapter(self, value):
        return self._set_prop('chapter', value)

    @property
    def screenshot_directory(self):
        return self._get_prop('screenshot_directory')

    @screenshot_directory.setter
    def screenshot_directory(self, value):
        return self._set_prop('screenshot_directory', value)

    @property
    def ao_null_format(self):
        return self._get_prop('ao_null_format')

    @ao_null_format.setter
    def ao_null_format(self, value):
        return self._set_prop('ao_null_format', value)

    @property
    def demuxer_lavf_probescore(self):
        return self._get_prop('demuxer_lavf_probescore')

    @demuxer_lavf_probescore.setter
    def demuxer_lavf_probescore(self, value):
        return self._set_prop('demuxer_lavf_probescore', value)

    @property
    def length(self):
        return self._get_prop('length')

    @length.setter
    def length(self, value):
        return self._set_prop('length', value)

    @property
    def vo_configured(self):
        return self._get_prop('vo_configured')

    @vo_configured.setter
    def vo_configured(self, value):
        return self._set_prop('vo_configured', value)

    @property
    def msg_level(self):
        return self._get_prop('msg_level')

    @msg_level.setter
    def msg_level(self, value):
        return self._set_prop('msg_level', value)

    @property
    def icc_3dlut_size(self):
        return self._get_prop('icc_3dlut_size')

    @icc_3dlut_size.setter
    def icc_3dlut_size(self, value):
        return self._set_prop('icc_3dlut_size', value)

    @property
    def sub_clear_on_seek(self):
        return self._get_prop('sub_clear_on_seek')

    @sub_clear_on_seek.setter
    def sub_clear_on_seek(self, value):
        return self._set_prop('sub_clear_on_seek', value)

    @property
    def colormatrix(self):
        return self._get_prop('colormatrix')

    @colormatrix.setter
    def colormatrix(self, value):
        return self._set_prop('colormatrix', value)

    @property
    def osd_sym_cc(self):
        return self._get_prop('osd_sym_cc')

    @osd_sym_cc.setter
    def osd_sym_cc(self, value):
        return self._set_prop('osd_sym_cc', value)

    @property
    def end(self):
        return self._get_prop('end')

    @end.setter
    def end(self, value):
        return self._set_prop('end', value)

    @property
    def sub_ass_force_margins(self):
        return self._get_prop('sub_ass_force_margins')

    @sub_ass_force_margins.setter
    def sub_ass_force_margins(self, value):
        return self._set_prop('sub_ass_force_margins', value)

    @property
    def scale_blur(self):
        return self._get_prop('scale_blur')

    @scale_blur.setter
    def scale_blur(self, value):
        return self._set_prop('scale_blur', value)

    @property
    def dvbin_timeout(self):
        return self._get_prop('dvbin_timeout')

    @dvbin_timeout.setter
    def dvbin_timeout(self, value):
        return self._set_prop('dvbin_timeout', value)

    @property
    def demuxer_start_time(self):
        return self._get_prop('demuxer_start_time')

    @demuxer_start_time.setter
    def demuxer_start_time(self, value):
        return self._set_prop('demuxer_start_time', value)

    @property
    def video_codec(self):
        return self._get_prop('video_codec')

    @video_codec.setter
    def video_codec(self, value):
        return self._set_prop('video_codec', value)

    @property
    def alsa_ignore_chmap(self):
        return self._get_prop('alsa_ignore_chmap')

    @alsa_ignore_chmap.setter
    def alsa_ignore_chmap(self, value):
        return self._set_prop('alsa_ignore_chmap', value)

    @property
    def wayland_app_id(self):
        return self._get_prop('wayland_app_id')

    @wayland_app_id.setter
    def wayland_app_id(self, value):
        return self._set_prop('wayland_app_id', value)

    @property
    def forcedsubsonly(self):
        return self._get_prop('forcedsubsonly')

    @forcedsubsonly.setter
    def forcedsubsonly(self, value):
        return self._set_prop('forcedsubsonly', value)

    @property
    def tscale_wtaper(self):
        return self._get_prop('tscale_wtaper')

    @tscale_wtaper.setter
    def tscale_wtaper(self, value):
        return self._set_prop('tscale_wtaper', value)

    @property
    def demuxer_mkv_probe_video_duration(self):
        return self._get_prop('demuxer_mkv_probe_video_duration')

    @demuxer_mkv_probe_video_duration.setter
    def demuxer_mkv_probe_video_duration(self, value):
        return self._set_prop('demuxer_mkv_probe_video_duration', value)

    @property
    def cdda_cdtext(self):
        return self._get_prop('cdda_cdtext')

    @cdda_cdtext.setter
    def cdda_cdtext(self, value):
        return self._set_prop('cdda_cdtext', value)

    @property
    def cdda_span_a(self):
        return self._get_prop('cdda_span_a')

    @cdda_span_a.setter
    def cdda_span_a(self, value):
        return self._set_prop('cdda_span_a', value)

    @property
    def vd_queue_max_bytes(self):
        return self._get_prop('vd_queue_max_bytes')

    @vd_queue_max_bytes.setter
    def vd_queue_max_bytes(self, value):
        return self._set_prop('vd_queue_max_bytes', value)

    @property
    def video_aspect(self):
        return self._get_prop('video_aspect')

    @video_aspect.setter
    def video_aspect(self, value):
        return self._set_prop('video_aspect', value)

    @property
    def media_keys(self):
        return self._get_prop('media_keys')

    @media_keys.setter
    def media_keys(self, value):
        return self._set_prop('media_keys', value)

    @property
    def ao_null_outburst(self):
        return self._get_prop('ao_null_outburst')

    @ao_null_outburst.setter
    def ao_null_outburst(self, value):
        return self._set_prop('ao_null_outburst', value)

    @property
    def demuxer_force_retry_on_eof(self):
        return self._get_prop('demuxer_force_retry_on_eof')

    @demuxer_force_retry_on_eof.setter
    def demuxer_force_retry_on_eof(self, value):
        return self._set_prop('demuxer_force_retry_on_eof', value)

    @property
    def keepaspect(self):
        return self._get_prop('keepaspect')

    @keepaspect.setter
    def keepaspect(self, value):
        return self._set_prop('keepaspect', value)

    @property
    def dscale_wparam(self):
        return self._get_prop('dscale_wparam')

    @dscale_wparam.setter
    def dscale_wparam(self, value):
        return self._set_prop('dscale_wparam', value)

    @property
    def force_window_position(self):
        return self._get_prop('force_window_position')

    @force_window_position.setter
    def force_window_position(self, value):
        return self._set_prop('force_window_position', value)

    @property
    def playback_time(self):
        return self._get_prop('playback_time')

    @playback_time.setter
    def playback_time(self, value):
        return self._set_prop('playback_time', value)

    @property
    def saturation(self):
        return self._get_prop('saturation')

    @saturation.setter
    def saturation(self, value):
        return self._set_prop('saturation', value)

    @property
    def sub_ass_shaper(self):
        return self._get_prop('sub_ass_shaper')

    @sub_ass_shaper.setter
    def sub_ass_shaper(self, value):
        return self._set_prop('sub_ass_shaper', value)

    @property
    def video_sync(self):
        return self._get_prop('video_sync')

    @video_sync.setter
    def video_sync(self, value):
        return self._set_prop('video_sync', value)

    @property
    def playback_abort(self):
        return self._get_prop('playback_abort')

    @playback_abort.setter
    def playback_abort(self, value):
        return self._set_prop('playback_abort', value)

    @property
    def drm_osd_size(self):
        return self._get_prop('drm_osd_size')

    @drm_osd_size.setter
    def drm_osd_size(self, value):
        return self._set_prop('drm_osd_size', value)

    @property
    def input_test(self):
        return self._get_prop('input_test')

    @input_test.setter
    def input_test(self, value):
        return self._set_prop('input_test', value)

    @property
    def term_title(self):
        return self._get_prop('term_title')

    @term_title.setter
    def term_title(self, value):
        return self._set_prop('term_title', value)

    @property
    def vf(self):
        return self._get_prop('vf')

    @vf.setter
    def vf(self, value):
        return self._set_prop('vf', value)

    @property
    def video_unscaled(self):
        return self._get_prop('video_unscaled')

    @video_unscaled.setter
    def video_unscaled(self, value):
        return self._set_prop('video_unscaled', value)

    @property
    def wid(self):
        return self._get_prop('wid')

    @wid.setter
    def wid(self, value):
        return self._set_prop('wid', value)

    @property
    def fit_border(self):
        return self._get_prop('fit_border')

    @fit_border.setter
    def fit_border(self, value):
        return self._set_prop('fit_border', value)

    @property
    def dvd_device(self):
        return self._get_prop('dvd_device')

    @dvd_device.setter
    def dvd_device(self, value):
        return self._set_prop('dvd_device', value)

    @property
    def osd_font_size(self):
        return self._get_prop('osd_font_size')

    @osd_font_size.setter
    def osd_font_size(self, value):
        return self._set_prop('osd_font_size', value)

    @property
    def cscale_wparam(self):
        return self._get_prop('cscale_wparam')

    @cscale_wparam.setter
    def cscale_wparam(self, value):
        return self._set_prop('cscale_wparam', value)

    @property
    def sub_align_x(self):
        return self._get_prop('sub_align_x')

    @sub_align_x.setter
    def sub_align_x(self, value):
        return self._set_prop('sub_align_x', value)

    @property
    def input_key_list(self):
        return self._get_prop('input_key_list')

    @input_key_list.setter
    def input_key_list(self, value):
        return self._set_prop('input_key_list', value)

    @property
    def loop_playlist(self):
        return self._get_prop('loop_playlist')

    @loop_playlist.setter
    def loop_playlist(self, value):
        return self._set_prop('loop_playlist', value)

    @property
    def alpha(self):
        return self._get_prop('alpha')

    @alpha.setter
    def alpha(self, value):
        return self._set_prop('alpha', value)

    @property
    def colormatrix_gamma(self):
        return self._get_prop('colormatrix_gamma')

    @colormatrix_gamma.setter
    def colormatrix_gamma(self, value):
        return self._set_prop('colormatrix_gamma', value)

    @property
    def oremove_metadata(self):
        return self._get_prop('oremove_metadata')

    @oremove_metadata.setter
    def oremove_metadata(self, value):
        return self._set_prop('oremove_metadata', value)

    @property
    def current_window_scale(self):
        return self._get_prop('current_window_scale')

    @current_window_scale.setter
    def current_window_scale(self, value):
        return self._set_prop('current_window_scale', value)

    @property
    def vid(self):
        return self._get_prop('vid')

    @vid.setter
    def vid(self, value):
        return self._set_prop('vid', value)

    @property
    def ass_force_style(self):
        return self._get_prop('ass_force_style')

    @ass_force_style.setter
    def ass_force_style(self, value):
        return self._set_prop('ass_force_style', value)

    @property
    def opengl_waitvsync(self):
        return self._get_prop('opengl_waitvsync')

    @opengl_waitvsync.setter
    def opengl_waitvsync(self, value):
        return self._set_prop('opengl_waitvsync', value)

    @property
    def shuffle(self):
        return self._get_prop('shuffle')

    @shuffle.setter
    def shuffle(self, value):
        return self._set_prop('shuffle', value)

    @property
    def current_edition(self):
        return self._get_prop('current_edition')

    @current_edition.setter
    def current_edition(self, value):
        return self._set_prop('current_edition', value)

    @property
    def sub_color(self):
        return self._get_prop('sub_color')

    @sub_color.setter
    def sub_color(self, value):
        return self._set_prop('sub_color', value)

    @property
    def audio_params(self):
        return self._get_prop('audio_params')

    @audio_params.setter
    def audio_params(self, value):
        return self._set_prop('audio_params', value)

    @property
    def osd_bold(self):
        return self._get_prop('osd_bold')

    @osd_bold.setter
    def osd_bold(self, value):
        return self._set_prop('osd_bold', value)

    @property
    def tone_mapping(self):
        return self._get_prop('tone_mapping')

    @tone_mapping.setter
    def tone_mapping(self, value):
        return self._set_prop('tone_mapping', value)

    @property
    def vd_lavc_software_fallback(self):
        return self._get_prop('vd_lavc_software_fallback')

    @vd_lavc_software_fallback.setter
    def vd_lavc_software_fallback(self, value):
        return self._set_prop('vd_lavc_software_fallback', value)

    @property
    def video_aspect_override(self):
        return self._get_prop('video_aspect_override')

    @video_aspect_override.setter
    def video_aspect_override(self, value):
        return self._set_prop('video_aspect_override', value)

    @property
    def sws_cvs(self):
        return self._get_prop('sws_cvs')

    @sws_cvs.setter
    def sws_cvs(self, value):
        return self._set_prop('sws_cvs', value)

    @property
    def brightness(self):
        return self._get_prop('brightness')

    @brightness.setter
    def brightness(self, value):
        return self._set_prop('brightness', value)

    @property
    def wayland_edge_pixels_pointer(self):
        return self._get_prop('wayland_edge_pixels_pointer')

    @wayland_edge_pixels_pointer.setter
    def wayland_edge_pixels_pointer(self, value):
        return self._set_prop('wayland_edge_pixels_pointer', value)

    @property
    def file_local_options(self):
        return self._get_prop('file_local_options')

    @file_local_options.setter
    def file_local_options(self, value):
        return self._set_prop('file_local_options', value)

    @property
    def right_alt_gr(self):
        return self._get_prop('right_alt_gr')

    @right_alt_gr.setter
    def right_alt_gr(self, value):
        return self._set_prop('right_alt_gr', value)

    @property
    def sub_font(self):
        return self._get_prop('sub_font')

    @sub_font.setter
    def sub_font(self, value):
        return self._set_prop('sub_font', value)

    @property
    def vo_image_webp_quality(self):
        return self._get_prop('vo_image_webp_quality')

    @vo_image_webp_quality.setter
    def vo_image_webp_quality(self, value):
        return self._set_prop('vo_image_webp_quality', value)

    @property
    def opengl_tex_pad_y(self):
        return self._get_prop('opengl_tex_pad_y')

    @opengl_tex_pad_y.setter
    def opengl_tex_pad_y(self, value):
        return self._set_prop('opengl_tex_pad_y', value)

    @property
    def override_display_fps(self):
        return self._get_prop('override_display_fps')

    @override_display_fps.setter
    def override_display_fps(self, value):
        return self._set_prop('override_display_fps', value)

    @property
    def sws_lgb(self):
        return self._get_prop('sws_lgb')

    @sws_lgb.setter
    def sws_lgb(self, value):
        return self._set_prop('sws_lgb', value)

    @property
    def tone_mapping_desaturate(self):
        return self._get_prop('tone_mapping_desaturate')

    @tone_mapping_desaturate.setter
    def tone_mapping_desaturate(self, value):
        return self._set_prop('tone_mapping_desaturate', value)

    @property
    def playlist_pos_1(self):
        return self._get_prop('playlist_pos_1')

    @playlist_pos_1.setter
    def playlist_pos_1(self, value):
        return self._set_prop('playlist_pos_1', value)

    @property
    def estimated_frame_count(self):
        return self._get_prop('estimated_frame_count')

    @estimated_frame_count.setter
    def estimated_frame_count(self, value):
        return self._set_prop('estimated_frame_count', value)

    @property
    def sub_ass_vsfilter_blur_compat(self):
        return self._get_prop('sub_ass_vsfilter_blur_compat')

    @sub_ass_vsfilter_blur_compat.setter
    def sub_ass_vsfilter_blur_compat(self, value):
        return self._set_prop('sub_ass_vsfilter_blur_compat', value)

    @property
    def vo_tct_256(self):
        return self._get_prop('vo_tct_256')

    @vo_tct_256.setter
    def vo_tct_256(self, value):
        return self._set_prop('vo_tct_256', value)

    @property
    def vsync_jitter(self):
        return self._get_prop('vsync_jitter')

    @vsync_jitter.setter
    def vsync_jitter(self, value):
        return self._set_prop('vsync_jitter', value)

    @property
    def load_stats_overlay(self):
        return self._get_prop('load_stats_overlay')

    @load_stats_overlay.setter
    def load_stats_overlay(self, value):
        return self._set_prop('load_stats_overlay', value)

    @property
    def sub_fps(self):
        return self._get_prop('sub_fps')

    @sub_fps.setter
    def sub_fps(self, value):
        return self._set_prop('sub_fps', value)

    @property
    def vd_lavc_skiploopfilter(self):
        return self._get_prop('vd_lavc_skiploopfilter')

    @vd_lavc_skiploopfilter.setter
    def vd_lavc_skiploopfilter(self, value):
        return self._set_prop('vd_lavc_skiploopfilter', value)

    @property
    def vo_vdpau_denoise(self):
        return self._get_prop('vo_vdpau_denoise')

    @vo_vdpau_denoise.setter
    def vo_vdpau_denoise(self, value):
        return self._set_prop('vo_vdpau_denoise', value)

    @property
    def osd_italic(self):
        return self._get_prop('osd_italic')

    @osd_italic.setter
    def osd_italic(self, value):
        return self._set_prop('osd_italic', value)

    @property
    def cscale_param1(self):
        return self._get_prop('cscale_param1')

    @cscale_param1.setter
    def cscale_param1(self, value):
        return self._set_prop('cscale_param1', value)

    @property
    def opengl_shaders(self):
        return self._get_prop('opengl_shaders')

    @opengl_shaders.setter
    def opengl_shaders(self, value):
        return self._set_prop('opengl_shaders', value)

    @property
    def x11_bypass_compositor(self):
        return self._get_prop('x11_bypass_compositor')

    @x11_bypass_compositor.setter
    def x11_bypass_compositor(self, value):
        return self._set_prop('x11_bypass_compositor', value)

    @property
    def deband_range(self):
        return self._get_prop('deband_range')

    @deband_range.setter
    def deband_range(self, value):
        return self._set_prop('deband_range', value)

    @property
    def sub_text_margin_y(self):
        return self._get_prop('sub_text_margin_y')

    @sub_text_margin_y.setter
    def sub_text_margin_y(self, value):
        return self._set_prop('sub_text_margin_y', value)

    @property
    def demuxer_lavf_o(self):
        return self._get_prop('demuxer_lavf_o')

    @demuxer_lavf_o.setter
    def demuxer_lavf_o(self, value):
        return self._set_prop('demuxer_lavf_o', value)

    @property
    def demuxer_readahead_secs(self):
        return self._get_prop('demuxer_readahead_secs')

    @demuxer_readahead_secs.setter
    def demuxer_readahead_secs(self, value):
        return self._set_prop('demuxer_readahead_secs', value)

    @property
    def vd_lavc_bitexact(self):
        return self._get_prop('vd_lavc_bitexact')

    @vd_lavc_bitexact.setter
    def vd_lavc_bitexact(self, value):
        return self._set_prop('vd_lavc_bitexact', value)

    @property
    def demuxer_cache_duration(self):
        return self._get_prop('demuxer_cache_duration')

    @demuxer_cache_duration.setter
    def demuxer_cache_duration(self, value):
        return self._set_prop('demuxer_cache_duration', value)

    @property
    def scale_wtaper(self):
        return self._get_prop('scale_wtaper')

    @scale_wtaper.setter
    def scale_wtaper(self, value):
        return self._set_prop('scale_wtaper', value)

    @property
    def osd_msg3(self):
        return self._get_prop('osd_msg3')

    @osd_msg3.setter
    def osd_msg3(self, value):
        return self._set_prop('osd_msg3', value)

    @property
    def ytdl_format(self):
        return self._get_prop('ytdl_format')

    @ytdl_format.setter
    def ytdl_format(self, value):
        return self._set_prop('ytdl_format', value)

    @property
    def ad_queue_max_secs(self):
        return self._get_prop('ad_queue_max_secs')

    @ad_queue_max_secs.setter
    def ad_queue_max_secs(self, value):
        return self._set_prop('ad_queue_max_secs', value)

    @property
    def gpu_shader_cache_dir(self):
        return self._get_prop('gpu_shader_cache_dir')

    @gpu_shader_cache_dir.setter
    def gpu_shader_cache_dir(self, value):
        return self._set_prop('gpu_shader_cache_dir', value)

    @property
    def load_auto_profiles(self):
        return self._get_prop('load_auto_profiles')

    @load_auto_profiles.setter
    def load_auto_profiles(self, value):
        return self._set_prop('load_auto_profiles', value)

    @property
    def vo_image_webp_lossless(self):
        return self._get_prop('vo_image_webp_lossless')

    @vo_image_webp_lossless.setter
    def vo_image_webp_lossless(self, value):
        return self._set_prop('vo_image_webp_lossless', value)

    @property
    def term_osd_bar_chars(self):
        return self._get_prop('term_osd_bar_chars')

    @term_osd_bar_chars.setter
    def term_osd_bar_chars(self, value):
        return self._set_prop('term_osd_bar_chars', value)

    @property
    def demuxer_lavf_format(self):
        return self._get_prop('demuxer_lavf_format')

    @demuxer_lavf_format.setter
    def demuxer_lavf_format(self, value):
        return self._set_prop('demuxer_lavf_format', value)

    @property
    def video_format(self):
        return self._get_prop('video_format')

    @video_format.setter
    def video_format(self, value):
        return self._set_prop('video_format', value)

    @property
    def audio_normalize_downmix(self):
        return self._get_prop('audio_normalize_downmix')

    @audio_normalize_downmix.setter
    def audio_normalize_downmix(self, value):
        return self._set_prop('audio_normalize_downmix', value)

    @property
    def osd_fractions(self):
        return self._get_prop('osd_fractions')

    @osd_fractions.setter
    def osd_fractions(self, value):
        return self._set_prop('osd_fractions', value)

    @property
    def vulkan_async_compute(self):
        return self._get_prop('vulkan_async_compute')

    @vulkan_async_compute.setter
    def vulkan_async_compute(self, value):
        return self._set_prop('vulkan_async_compute', value)

    @property
    def input_default_bindings(self):
        return self._get_prop('input_default_bindings')

    @input_default_bindings.setter
    def input_default_bindings(self, value):
        return self._set_prop('input_default_bindings', value)

    @property
    def dscale_clamp(self):
        return self._get_prop('dscale_clamp')

    @dscale_clamp.setter
    def dscale_clamp(self, value):
        return self._set_prop('dscale_clamp', value)

    @property
    def opengl_fbo_format(self):
        return self._get_prop('opengl_fbo_format')

    @opengl_fbo_format.setter
    def opengl_fbo_format(self, value):
        return self._set_prop('opengl_fbo_format', value)

    @property
    def audio_resample_cutoff(self):
        return self._get_prop('audio_resample_cutoff')

    @audio_resample_cutoff.setter
    def audio_resample_cutoff(self, value):
        return self._set_prop('audio_resample_cutoff', value)

    @property
    def force_window(self):
        return self._get_prop('force_window')

    @force_window.setter
    def force_window(self, value):
        return self._set_prop('force_window', value)

    @property
    def hdr_peak_decay_rate(self):
        return self._get_prop('hdr_peak_decay_rate')

    @hdr_peak_decay_rate.setter
    def hdr_peak_decay_rate(self, value):
        return self._set_prop('hdr_peak_decay_rate', value)

    @property
    def tscale(self):
        return self._get_prop('tscale')

    @tscale.setter
    def tscale(self, value):
        return self._set_prop('tscale', value)

    @property
    def working_directory(self):
        return self._get_prop('working_directory')

    @working_directory.setter
    def working_directory(self, value):
        return self._set_prop('working_directory', value)

    @property
    def video_scale_x(self):
        return self._get_prop('video_scale_x')

    @video_scale_x.setter
    def video_scale_x(self, value):
        return self._set_prop('video_scale_x', value)

    @property
    def tscale_wblur(self):
        return self._get_prop('tscale_wblur')

    @tscale_wblur.setter
    def tscale_wblur(self, value):
        return self._set_prop('tscale_wblur', value)

    @property
    def audio_backward_batch(self):
        return self._get_prop('audio_backward_batch')

    @audio_backward_batch.setter
    def audio_backward_batch(self, value):
        return self._set_prop('audio_backward_batch', value)

    @property
    def linear_upscaling(self):
        return self._get_prop('linear_upscaling')

    @linear_upscaling.setter
    def linear_upscaling(self, value):
        return self._set_prop('linear_upscaling', value)

    @property
    def gpu_debug(self):
        return self._get_prop('gpu_debug')

    @gpu_debug.setter
    def gpu_debug(self, value):
        return self._set_prop('gpu_debug', value)

    @property
    def autofit_smaller(self):
        return self._get_prop('autofit_smaller')

    @autofit_smaller.setter
    def autofit_smaller(self, value):
        return self._set_prop('autofit_smaller', value)

    @property
    def quiet(self):
        return self._get_prop('quiet')

    @quiet.setter
    def quiet(self, value):
        return self._set_prop('quiet', value)

    @property
    def sub_text_align_x(self):
        return self._get_prop('sub_text_align_x')

    @sub_text_align_x.setter
    def sub_text_align_x(self, value):
        return self._set_prop('sub_text_align_x', value)

    @property
    def scale_antiring(self):
        return self._get_prop('scale_antiring')

    @scale_antiring.setter
    def scale_antiring(self, value):
        return self._set_prop('scale_antiring', value)

    @property
    def teletext_page(self):
        return self._get_prop('teletext_page')

    @teletext_page.setter
    def teletext_page(self, value):
        return self._set_prop('teletext_page', value)

    @property
    def ad_lavc_threads(self):
        return self._get_prop('ad_lavc_threads')

    @ad_lavc_threads.setter
    def ad_lavc_threads(self, value):
        return self._set_prop('ad_lavc_threads', value)

    @property
    def hwdec_interop(self):
        return self._get_prop('hwdec_interop')

    @hwdec_interop.setter
    def hwdec_interop(self, value):
        return self._set_prop('hwdec_interop', value)

    @property
    def filename(self):
        return self._get_prop('filename')

    @filename.setter
    def filename(self, value):
        return self._set_prop('filename', value)

    @property
    def vo_vaapi_scaled_osd(self):
        return self._get_prop('vo_vaapi_scaled_osd')

    @vo_vaapi_scaled_osd.setter
    def vo_vaapi_scaled_osd(self, value):
        return self._set_prop('vo_vaapi_scaled_osd', value)

    @property
    def vo_image_webp_compression(self):
        return self._get_prop('vo_image_webp_compression')

    @vo_image_webp_compression.setter
    def vo_image_webp_compression(self, value):
        return self._set_prop('vo_image_webp_compression', value)

    @property
    def glsl_shaders(self):
        return self._get_prop('glsl_shaders')

    @glsl_shaders.setter
    def glsl_shaders(self, value):
        return self._set_prop('glsl_shaders', value)

    @property
    def hdr_tone_mapping(self):
        return self._get_prop('hdr_tone_mapping')

    @hdr_tone_mapping.setter
    def hdr_tone_mapping(self, value):
        return self._set_prop('hdr_tone_mapping', value)

    @property
    def opengl_backend(self):
        return self._get_prop('opengl_backend')

    @opengl_backend.setter
    def opengl_backend(self, value):
        return self._set_prop('opengl_backend', value)

    @property
    def opengl_gamma(self):
        return self._get_prop('opengl_gamma')

    @opengl_gamma.setter
    def opengl_gamma(self, value):
        return self._set_prop('opengl_gamma', value)

    @property
    def stop_xscreensaver(self):
        return self._get_prop('stop_xscreensaver')

    @stop_xscreensaver.setter
    def stop_xscreensaver(self, value):
        return self._set_prop('stop_xscreensaver', value)

    @property
    def osd_par(self):
        return self._get_prop('osd_par')

    @osd_par.setter
    def osd_par(self, value):
        return self._set_prop('osd_par', value)

    @property
    def subs_with_matching_audio(self):
        return self._get_prop('subs_with_matching_audio')

    @subs_with_matching_audio.setter
    def subs_with_matching_audio(self, value):
        return self._set_prop('subs_with_matching_audio', value)

    @property
    def vd_lavc_skipidct(self):
        return self._get_prop('vd_lavc_skipidct')

    @vd_lavc_skipidct.setter
    def vd_lavc_skipidct(self, value):
        return self._set_prop('vd_lavc_skipidct', value)

    @property
    def force_media_title(self):
        return self._get_prop('force_media_title')

    @force_media_title.setter
    def force_media_title(self, value):
        return self._set_prop('force_media_title', value)

    @property
    def file_format(self):
        return self._get_prop('file_format')

    @file_format.setter
    def file_format(self, value):
        return self._set_prop('file_format', value)

    @property
    def scripts(self):
        return self._get_prop('scripts')

    @scripts.setter
    def scripts(self, value):
        return self._set_prop('scripts', value)

    @property
    def current_demuxer(self):
        return self._get_prop('current_demuxer')

    @current_demuxer.setter
    def current_demuxer(self, value):
        return self._set_prop('current_demuxer', value)

    @property
    def geometry(self):
        return self._get_prop('geometry')

    @geometry.setter
    def geometry(self, value):
        return self._set_prop('geometry', value)

    @property
    def force_seekable(self):
        return self._get_prop('force_seekable')

    @force_seekable.setter
    def force_seekable(self, value):
        return self._set_prop('force_seekable', value)

    @property
    def initial_audio_sync(self):
        return self._get_prop('initial_audio_sync')

    @initial_audio_sync.setter
    def initial_audio_sync(self, value):
        return self._set_prop('initial_audio_sync', value)

    @property
    def screenshot_jpeg_source_chroma(self):
        return self._get_prop('screenshot_jpeg_source_chroma')

    @screenshot_jpeg_source_chroma.setter
    def screenshot_jpeg_source_chroma(self, value):
        return self._set_prop('screenshot_jpeg_source_chroma', value)

    @property
    def access_references(self):
        return self._get_prop('access_references')

    @access_references.setter
    def access_references(self, value):
        return self._set_prop('access_references', value)

    @property
    def sub_back_color(self):
        return self._get_prop('sub_back_color')

    @sub_back_color.setter
    def sub_back_color(self, value):
        return self._set_prop('sub_back_color', value)

    @property
    def video_margin_ratio_top(self):
        return self._get_prop('video_margin_ratio_top')

    @video_margin_ratio_top.setter
    def video_margin_ratio_top(self, value):
        return self._set_prop('video_margin_ratio_top', value)

    @property
    def vo_tct_height(self):
        return self._get_prop('vo_tct_height')

    @vo_tct_height.setter
    def vo_tct_height(self, value):
        return self._set_prop('vo_tct_height', value)

    @property
    def input_x11_keyboard(self):
        return self._get_prop('input_x11_keyboard')

    @input_x11_keyboard.setter
    def input_x11_keyboard(self, value):
        return self._set_prop('input_x11_keyboard', value)

    @property
    def osd_margin_y(self):
        return self._get_prop('osd_margin_y')

    @osd_margin_y.setter
    def osd_margin_y(self, value):
        return self._set_prop('osd_margin_y', value)

    @property
    def msg_color(self):
        return self._get_prop('msg_color')

    @msg_color.setter
    def msg_color(self, value):
        return self._set_prop('msg_color', value)

    @property
    def sub_visibility(self):
        return self._get_prop('sub_visibility')

    @sub_visibility.setter
    def sub_visibility(self, value):
        return self._set_prop('sub_visibility', value)

    @property
    def demuxer_backward_playback_step(self):
        return self._get_prop('demuxer_backward_playback_step')

    @demuxer_backward_playback_step.setter
    def demuxer_backward_playback_step(self, value):
        return self._set_prop('demuxer_backward_playback_step', value)

    @property
    def alang(self):
        return self._get_prop('alang')

    @alang.setter
    def alang(self, value):
        return self._set_prop('alang', value)

    @property
    def cscale_wtaper(self):
        return self._get_prop('cscale_wtaper')

    @cscale_wtaper.setter
    def cscale_wtaper(self, value):
        return self._set_prop('cscale_wtaper', value)

    @property
    def vo_image_tag_colorspace(self):
        return self._get_prop('vo_image_tag_colorspace')

    @vo_image_tag_colorspace.setter
    def vo_image_tag_colorspace(self, value):
        return self._set_prop('vo_image_tag_colorspace', value)

    @property
    def msgcolor(self):
        return self._get_prop('msgcolor')

    @msgcolor.setter
    def msgcolor(self, value):
        return self._set_prop('msgcolor', value)

    @property
    def track_list(self):
        return self._get_prop('track_list')

    @track_list.setter
    def track_list(self, value):
        return self._set_prop('track_list', value)

    @property
    def xv_port(self):
        return self._get_prop('xv_port')

    @xv_port.setter
    def xv_port(self, value):
        return self._set_prop('xv_port', value)

    @property
    def secondary_sid(self):
        return self._get_prop('secondary_sid')

    @secondary_sid.setter
    def secondary_sid(self, value):
        return self._set_prop('secondary_sid', value)

    @property
    def osd_align_x(self):
        return self._get_prop('osd_align_x')

    @osd_align_x.setter
    def osd_align_x(self, value):
        return self._set_prop('osd_align_x', value)

    @property
    def display_names(self):
        return self._get_prop('display_names')

    @display_names.setter
    def display_names(self, value):
        return self._set_prop('display_names', value)

    @property
    def ao_null_untimed(self):
        return self._get_prop('ao_null_untimed')

    @ao_null_untimed.setter
    def ao_null_untimed(self, value):
        return self._set_prop('ao_null_untimed', value)

    @property
    def font(self):
        return self._get_prop('font')

    @font.setter
    def font(self, value):
        return self._set_prop('font', value)

    @property
    def input_terminal(self):
        return self._get_prop('input_terminal')

    @input_terminal.setter
    def input_terminal(self, value):
        return self._set_prop('input_terminal', value)

    @property
    def interpolation(self):
        return self._get_prop('interpolation')

    @interpolation.setter
    def interpolation(self, value):
        return self._set_prop('interpolation', value)

    @property
    def clock(self):
        return self._get_prop('clock')

    @clock.setter
    def clock(self, value):
        return self._set_prop('clock', value)

    @property
    def gamut_warning(self):
        return self._get_prop('gamut_warning')

    @gamut_warning.setter
    def gamut_warning(self, value):
        return self._set_prop('gamut_warning', value)

    @property
    def strict(self):
        return self._get_prop('strict')

    @strict.setter
    def strict(self, value):
        return self._set_prop('strict', value)

    @property
    def overlays(self):
        return self._get_prop('overlays')

    @overlays.setter
    def overlays(self, value):
        return self._set_prop('overlays', value)

    @property
    def reset_on_next_file(self):
        return self._get_prop('reset_on_next_file')

    @reset_on_next_file.setter
    def reset_on_next_file(self, value):
        return self._set_prop('reset_on_next_file', value)

    @property
    def video_zoom(self):
        return self._get_prop('video_zoom')

    @video_zoom.setter
    def video_zoom(self, value):
        return self._set_prop('video_zoom', value)

    @property
    def endpos(self):
        return self._get_prop('endpos')

    @endpos.setter
    def endpos(self, value):
        return self._set_prop('endpos', value)

    @property
    def video_backward_batch(self):
        return self._get_prop('video_backward_batch')

    @video_backward_batch.setter
    def video_backward_batch(self, value):
        return self._set_prop('video_backward_batch', value)

    @property
    def audio_resample_max_output_size(self):
        return self._get_prop('audio_resample_max_output_size')

    @audio_resample_max_output_size.setter
    def audio_resample_max_output_size(self, value):
        return self._set_prop('audio_resample_max_output_size', value)

    @property
    def monitorpixelaspect(self):
        return self._get_prop('monitorpixelaspect')

    @monitorpixelaspect.setter
    def monitorpixelaspect(self, value):
        return self._set_prop('monitorpixelaspect', value)

    @property
    def zimg_scaler(self):
        return self._get_prop('zimg_scaler')

    @zimg_scaler.setter
    def zimg_scaler(self, value):
        return self._set_prop('zimg_scaler', value)

    @property
    def mf_type(self):
        return self._get_prop('mf_type')

    @mf_type.setter
    def mf_type(self, value):
        return self._set_prop('mf_type', value)

    @property
    def demuxer_lavf_probe_info(self):
        return self._get_prop('demuxer_lavf_probe_info')

    @demuxer_lavf_probe_info.setter
    def demuxer_lavf_probe_info(self, value):
        return self._set_prop('demuxer_lavf_probe_info', value)

    @property
    def input_key_fifo_size(self):
        return self._get_prop('input_key_fifo_size')

    @input_key_fifo_size.setter
    def input_key_fifo_size(self, value):
        return self._set_prop('input_key_fifo_size', value)

    @property
    def vulkan_queue_count(self):
        return self._get_prop('vulkan_queue_count')

    @vulkan_queue_count.setter
    def vulkan_queue_count(self, value):
        return self._set_prop('vulkan_queue_count', value)

    @property
    def tscale_param2(self):
        return self._get_prop('tscale_param2')

    @tscale_param2.setter
    def tscale_param2(self, value):
        return self._set_prop('tscale_param2', value)

    @property
    def hidpi_window_scale(self):
        return self._get_prop('hidpi_window_scale')

    @hidpi_window_scale.setter
    def hidpi_window_scale(self, value):
        return self._set_prop('hidpi_window_scale', value)

    @property
    def dvbin_full_transponder(self):
        return self._get_prop('dvbin_full_transponder')

    @dvbin_full_transponder.setter
    def dvbin_full_transponder(self, value):
        return self._set_prop('dvbin_full_transponder', value)

    @property
    def osd_bar_align_x(self):
        return self._get_prop('osd_bar_align_x')

    @osd_bar_align_x.setter
    def osd_bar_align_x(self, value):
        return self._set_prop('osd_bar_align_x', value)

    @property
    def tscale_window(self):
        return self._get_prop('tscale_window')

    @tscale_window.setter
    def tscale_window(self, value):
        return self._set_prop('tscale_window', value)

    @property
    def monitoraspect(self):
        return self._get_prop('monitoraspect')

    @monitoraspect.setter
    def monitoraspect(self, value):
        return self._set_prop('monitoraspect', value)

    @property
    def sub_filter_sdh_harder(self):
        return self._get_prop('sub_filter_sdh_harder')

    @sub_filter_sdh_harder.setter
    def sub_filter_sdh_harder(self, value):
        return self._set_prop('sub_filter_sdh_harder', value)

    @property
    def drm_mode(self):
        return self._get_prop('drm_mode')

    @drm_mode.setter
    def drm_mode(self, value):
        return self._set_prop('drm_mode', value)

    @property
    def forceidx(self):
        return self._get_prop('forceidx')

    @forceidx.setter
    def forceidx(self, value):
        return self._set_prop('forceidx', value)

    @property
    def chapters_file(self):
        return self._get_prop('chapters_file')

    @chapters_file.setter
    def chapters_file(self, value):
        return self._set_prop('chapters_file', value)

    @property
    def ao_null_buffer(self):
        return self._get_prop('ao_null_buffer')

    @ao_null_buffer.setter
    def ao_null_buffer(self, value):
        return self._set_prop('ao_null_buffer', value)

    @property
    def demuxer_lavf_allow_mimetype(self):
        return self._get_prop('demuxer_lavf_allow_mimetype')

    @demuxer_lavf_allow_mimetype.setter
    def demuxer_lavf_allow_mimetype(self, value):
        return self._set_prop('demuxer_lavf_allow_mimetype', value)

    @property
    def window_scale(self):
        return self._get_prop('window_scale')

    @window_scale.setter
    def window_scale(self, value):
        return self._set_prop('window_scale', value)

    @property
    def correct_pts(self):
        return self._get_prop('correct_pts')

    @correct_pts.setter
    def correct_pts(self, value):
        return self._set_prop('correct_pts', value)

    @property
    def demuxer_rawvideo_w(self):
        return self._get_prop('demuxer_rawvideo_w')

    @demuxer_rawvideo_w.setter
    def demuxer_rawvideo_w(self, value):
        return self._set_prop('demuxer_rawvideo_w', value)

    @property
    def osd_blur(self):
        return self._get_prop('osd_blur')

    @osd_blur.setter
    def osd_blur(self, value):
        return self._set_prop('osd_blur', value)

    @property
    def osd_playing_msg(self):
        return self._get_prop('osd_playing_msg')

    @osd_playing_msg.setter
    def osd_playing_msg(self, value):
        return self._set_prop('osd_playing_msg', value)

    @property
    def ad_queue_max_samples(self):
        return self._get_prop('ad_queue_max_samples')

    @ad_queue_max_samples.setter
    def ad_queue_max_samples(self, value):
        return self._set_prop('ad_queue_max_samples', value)

    @property
    def profile_list(self):
        return self._get_prop('profile_list')

    @profile_list.setter
    def profile_list(self, value):
        return self._set_prop('profile_list', value)

    @property
    def interpolation_threshold(self):
        return self._get_prop('interpolation_threshold')

    @interpolation_threshold.setter
    def interpolation_threshold(self, value):
        return self._set_prop('interpolation_threshold', value)

    @property
    def jack_name(self):
        return self._get_prop('jack_name')

    @jack_name.setter
    def jack_name(self, value):
        return self._set_prop('jack_name', value)

    @property
    def pulse_buffer(self):
        return self._get_prop('pulse_buffer')

    @pulse_buffer.setter
    def pulse_buffer(self, value):
        return self._set_prop('pulse_buffer', value)

    @property
    def sub_font_provider(self):
        return self._get_prop('sub_font_provider')

    @sub_font_provider.setter
    def sub_font_provider(self, value):
        return self._set_prop('sub_font_provider', value)

    @property
    def subdelay(self):
        return self._get_prop('subdelay')

    @subdelay.setter
    def subdelay(self, value):
        return self._set_prop('subdelay', value)

    @property
    def screenshot_jpeg_quality(self):
        return self._get_prop('screenshot_jpeg_quality')

    @screenshot_jpeg_quality.setter
    def screenshot_jpeg_quality(self, value):
        return self._set_prop('screenshot_jpeg_quality', value)

    @property
    def icc_profile_auto(self):
        return self._get_prop('icc_profile_auto')

    @icc_profile_auto.setter
    def icc_profile_auto(self, value):
        return self._set_prop('icc_profile_auto', value)

    @property
    def eof_reached(self):
        return self._get_prop('eof_reached')

    @eof_reached.setter
    def eof_reached(self, value):
        return self._set_prop('eof_reached', value)

    @property
    def mpv_version(self):
        return self._get_prop('mpv_version')

    @mpv_version.setter
    def mpv_version(self, value):
        return self._set_prop('mpv_version', value)

    @property
    def opengl_rectangle_textures(self):
        return self._get_prop('opengl_rectangle_textures')

    @opengl_rectangle_textures.setter
    def opengl_rectangle_textures(self, value):
        return self._set_prop('opengl_rectangle_textures', value)

    @property
    def stream_lavf_o(self):
        return self._get_prop('stream_lavf_o')

    @stream_lavf_o.setter
    def stream_lavf_o(self, value):
        return self._set_prop('stream_lavf_o', value)

    @property
    def edition_list(self):
        return self._get_prop('edition_list')

    @edition_list.setter
    def edition_list(self, value):
        return self._set_prop('edition_list', value)

    @property
    def vulkan_device(self):
        return self._get_prop('vulkan_device')

    @vulkan_device.setter
    def vulkan_device(self, value):
        return self._set_prop('vulkan_device', value)

    @property
    def hr_seek(self):
        return self._get_prop('hr_seek')

    @hr_seek.setter
    def hr_seek(self, value):
        return self._set_prop('hr_seek', value)

    @property
    def osd_scale(self):
        return self._get_prop('osd_scale')

    @osd_scale.setter
    def osd_scale(self, value):
        return self._set_prop('osd_scale', value)

    @property
    def sigmoid_center(self):
        return self._get_prop('sigmoid_center')

    @sigmoid_center.setter
    def sigmoid_center(self, value):
        return self._set_prop('sigmoid_center', value)

    @property
    def pulse_latency_hacks(self):
        return self._get_prop('pulse_latency_hacks')

    @pulse_latency_hacks.setter
    def pulse_latency_hacks(self, value):
        return self._set_prop('pulse_latency_hacks', value)

    @property
    def audio_samplerate(self):
        return self._get_prop('audio_samplerate')

    @audio_samplerate.setter
    def audio_samplerate(self, value):
        return self._set_prop('audio_samplerate', value)

    @property
    def core_shutdown(self):
        return self._get_prop('core_shutdown')

    @core_shutdown.setter
    def core_shutdown(self, value):
        return self._set_prop('core_shutdown', value)

    @property
    def screenshot_tag_colorspace(self):
        return self._get_prop('screenshot_tag_colorspace')

    @screenshot_tag_colorspace.setter
    def screenshot_tag_colorspace(self, value):
        return self._set_prop('screenshot_tag_colorspace', value)

    @property
    def stretch_dvd_subs(self):
        return self._get_prop('stretch_dvd_subs')

    @stretch_dvd_subs.setter
    def stretch_dvd_subs(self, value):
        return self._set_prop('stretch_dvd_subs', value)

    @property
    def tscale_param1(self):
        return self._get_prop('tscale_param1')

    @tscale_param1.setter
    def tscale_param1(self, value):
        return self._set_prop('tscale_param1', value)

    @property
    def vo_vdpau_chroma_deint(self):
        return self._get_prop('vo_vdpau_chroma_deint')

    @vo_vdpau_chroma_deint.setter
    def vo_vdpau_chroma_deint(self, value):
        return self._set_prop('vo_vdpau_chroma_deint', value)

    @property
    def ao_null_broken_delay(self):
        return self._get_prop('ao_null_broken_delay')

    @ao_null_broken_delay.setter
    def ao_null_broken_delay(self, value):
        return self._set_prop('ao_null_broken_delay', value)

    @property
    def sws_chs(self):
        return self._get_prop('sws_chs')

    @sws_chs.setter
    def sws_chs(self, value):
        return self._set_prop('sws_chs', value)

    @property
    def packet_sub_bitrate(self):
        return self._get_prop('packet_sub_bitrate')

    @packet_sub_bitrate.setter
    def packet_sub_bitrate(self, value):
        return self._set_prop('packet_sub_bitrate', value)

    @property
    def ass_vsfilter_aspect_compat(self):
        return self._get_prop('ass_vsfilter_aspect_compat')

    @ass_vsfilter_aspect_compat.setter
    def ass_vsfilter_aspect_compat(self, value):
        return self._set_prop('ass_vsfilter_aspect_compat', value)

    @property
    def audio_demuxer(self):
        return self._get_prop('audio_demuxer')

    @audio_demuxer.setter
    def audio_demuxer(self, value):
        return self._set_prop('audio_demuxer', value)

    @property
    def cscale(self):
        return self._get_prop('cscale')

    @cscale.setter
    def cscale(self, value):
        return self._set_prop('cscale', value)

    @property
    def x11_netwm(self):
        return self._get_prop('x11_netwm')

    @x11_netwm.setter
    def x11_netwm(self, value):
        return self._set_prop('x11_netwm', value)

    @property
    def cdda_overlap(self):
        return self._get_prop('cdda_overlap')

    @cdda_overlap.setter
    def cdda_overlap(self, value):
        return self._set_prop('cdda_overlap', value)

    @property
    def display_sync_active(self):
        return self._get_prop('display_sync_active')

    @display_sync_active.setter
    def display_sync_active(self, value):
        return self._set_prop('display_sync_active', value)

    @property
    def wayland_disable_vsync(self):
        return self._get_prop('wayland_disable_vsync')

    @wayland_disable_vsync.setter
    def wayland_disable_vsync(self, value):
        return self._set_prop('wayland_disable_vsync', value)

    @property
    def dither_size_fruit(self):
        return self._get_prop('dither_size_fruit')

    @dither_size_fruit.setter
    def dither_size_fruit(self, value):
        return self._set_prop('dither_size_fruit', value)

    @property
    def audio_channels(self):
        return self._get_prop('audio_channels')

    @audio_channels.setter
    def audio_channels(self, value):
        return self._set_prop('audio_channels', value)

    @property
    def opengl_early_flush(self):
        return self._get_prop('opengl_early_flush')

    @opengl_early_flush.setter
    def opengl_early_flush(self, value):
        return self._set_prop('opengl_early_flush', value)

    @property
    def error_diffusion(self):
        return self._get_prop('error_diffusion')

    @error_diffusion.setter
    def error_diffusion(self, value):
        return self._set_prop('error_diffusion', value)

    @property
    def idle(self):
        return self._get_prop('idle')

    @idle.setter
    def idle(self, value):
        return self._set_prop('idle', value)

    @property
    def osd_dimensions(self):
        return self._get_prop('osd_dimensions')

    @osd_dimensions.setter
    def osd_dimensions(self, value):
        return self._set_prop('osd_dimensions', value)

    @property
    def screenshot_webp_lossless(self):
        return self._get_prop('screenshot_webp_lossless')

    @screenshot_webp_lossless.setter
    def screenshot_webp_lossless(self, value):
        return self._set_prop('screenshot_webp_lossless', value)

    @property
    def sws_cgb(self):
        return self._get_prop('sws_cgb')

    @sws_cgb.setter
    def sws_cgb(self, value):
        return self._set_prop('sws_cgb', value)

    @property
    def vd_queue_max_secs(self):
        return self._get_prop('vd_queue_max_secs')

    @vd_queue_max_secs.setter
    def vd_queue_max_secs(self, value):
        return self._set_prop('vd_queue_max_secs', value)

    @property
    def video_aspect_method(self):
        return self._get_prop('video_aspect_method')

    @video_aspect_method.setter
    def video_aspect_method(self, value):
        return self._set_prop('video_aspect_method', value)

    @property
    def osd_bar_align_y(self):
        return self._get_prop('osd_bar_align_y')

    @osd_bar_align_y.setter
    def osd_bar_align_y(self, value):
        return self._set_prop('osd_bar_align_y', value)

    @property
    def edition(self):
        return self._get_prop('edition')

    @edition.setter
    def edition(self, value):
        return self._set_prop('edition', value)

    @property
    def demuxer_cache_idle(self):
        return self._get_prop('demuxer_cache_idle')

    @demuxer_cache_idle.setter
    def demuxer_cache_idle(self, value):
        return self._set_prop('demuxer_cache_idle', value)

    @property
    def sub_gray(self):
        return self._get_prop('sub_gray')

    @sub_gray.setter
    def sub_gray(self, value):
        return self._set_prop('sub_gray', value)

    @property
    def video_margin_ratio_bottom(self):
        return self._get_prop('video_margin_ratio_bottom')

    @video_margin_ratio_bottom.setter
    def video_margin_ratio_bottom(self, value):
        return self._set_prop('video_margin_ratio_bottom', value)

    @property
    def stream_open_filename(self):
        return self._get_prop('stream_open_filename')

    @stream_open_filename.setter
    def stream_open_filename(self, value):
        return self._set_prop('stream_open_filename', value)

    @property
    def estimated_frame_number(self):
        return self._get_prop('estimated_frame_number')

    @estimated_frame_number.setter
    def estimated_frame_number(self, value):
        return self._set_prop('estimated_frame_number', value)

    @property
    def ass_force_margins(self):
        return self._get_prop('ass_force_margins')

    @ass_force_margins.setter
    def ass_force_margins(self, value):
        return self._set_prop('ass_force_margins', value)

    @property
    def jack_connect(self):
        return self._get_prop('jack_connect')

    @jack_connect.setter
    def jack_connect(self, value):
        return self._set_prop('jack_connect', value)

    @property
    def load_osd_console(self):
        return self._get_prop('load_osd_console')

    @load_osd_console.setter
    def load_osd_console(self, value):
        return self._set_prop('load_osd_console', value)

    @property
    def temporal_dither_period(self):
        return self._get_prop('temporal_dither_period')

    @temporal_dither_period.setter
    def temporal_dither_period(self, value):
        return self._set_prop('temporal_dither_period', value)

    @property
    def http_header_fields(self):
        return self._get_prop('http_header_fields')

    @http_header_fields.setter
    def http_header_fields(self, value):
        return self._set_prop('http_header_fields', value)

    @property
    def gpu_context(self):
        return self._get_prop('gpu_context')

    @gpu_context.setter
    def gpu_context(self, value):
        return self._set_prop('gpu_context', value)

    @property
    def ao_pcm_append(self):
        return self._get_prop('ao_pcm_append')

    @ao_pcm_append.setter
    def ao_pcm_append(self, value):
        return self._set_prop('ao_pcm_append', value)

    @property
    def osd_scale_by_window(self):
        return self._get_prop('osd_scale_by_window')

    @osd_scale_by_window.setter
    def osd_scale_by_window(self, value):
        return self._set_prop('osd_scale_by_window', value)

    @property
    def opengl_check_pattern_a(self):
        return self._get_prop('opengl_check_pattern_a')

    @opengl_check_pattern_a.setter
    def opengl_check_pattern_a(self, value):
        return self._set_prop('opengl_check_pattern_a', value)

    @property
    def mistimed_frame_count(self):
        return self._get_prop('mistimed_frame_count')

    @mistimed_frame_count.setter
    def mistimed_frame_count(self, value):
        return self._set_prop('mistimed_frame_count', value)

    @property
    def spirv_compiler(self):
        return self._get_prop('spirv_compiler')

    @spirv_compiler.setter
    def spirv_compiler(self, value):
        return self._set_prop('spirv_compiler', value)

    @property
    def vo_delayed_frame_count(self):
        return self._get_prop('vo_delayed_frame_count')

    @vo_delayed_frame_count.setter
    def vo_delayed_frame_count(self, value):
        return self._set_prop('vo_delayed_frame_count', value)

    @property
    def sub(self):
        return self._get_prop('sub')

    @sub.setter
    def sub(self, value):
        return self._set_prop('sub', value)

    @property
    def jack_std_channel_layout(self):
        return self._get_prop('jack_std_channel_layout')

    @jack_std_channel_layout.setter
    def jack_std_channel_layout(self, value):
        return self._set_prop('jack_std_channel_layout', value)

    @property
    def sub_border_size(self):
        return self._get_prop('sub_border_size')

    @sub_border_size.setter
    def sub_border_size(self, value):
        return self._set_prop('sub_border_size', value)

    @property
    def start(self):
        return self._get_prop('start')

    @start.setter
    def start(self, value):
        return self._set_prop('start', value)

    @property
    def mute(self):
        return self._get_prop('mute')

    @mute.setter
    def mute(self, value):
        return self._set_prop('mute', value)

    @property
    def subfps(self):
        return self._get_prop('subfps')

    @subfps.setter
    def subfps(self, value):
        return self._set_prop('subfps', value)

    @property
    def video_backward_overlap(self):
        return self._get_prop('video_backward_overlap')

    @video_backward_overlap.setter
    def video_backward_overlap(self, value):
        return self._set_prop('video_backward_overlap', value)

    @property
    def scaler_lut_size(self):
        return self._get_prop('scaler_lut_size')

    @scaler_lut_size.setter
    def scaler_lut_size(self, value):
        return self._set_prop('scaler_lut_size', value)

    @property
    def audio_file_auto(self):
        return self._get_prop('audio_file_auto')

    @audio_file_auto.setter
    def audio_file_auto(self, value):
        return self._set_prop('audio_file_auto', value)

    @property
    def input_ipc_server(self):
        return self._get_prop('input_ipc_server')

    @input_ipc_server.setter
    def input_ipc_server(self, value):
        return self._set_prop('input_ipc_server', value)

    @property
    def external_files(self):
        return self._get_prop('external_files')

    @external_files.setter
    def external_files(self, value):
        return self._set_prop('external_files', value)

    @property
    def subfont(self):
        return self._get_prop('subfont')

    @subfont.setter
    def subfont(self, value):
        return self._set_prop('subfont', value)

    @property
    def input_unix_socket(self):
        return self._get_prop('input_unix_socket')

    @input_unix_socket.setter
    def input_unix_socket(self, value):
        return self._set_prop('input_unix_socket', value)

    @property
    def screenshot_template(self):
        return self._get_prop('screenshot_template')

    @screenshot_template.setter
    def screenshot_template(self, value):
        return self._set_prop('screenshot_template', value)

    @property
    def colormatrix_primaries(self):
        return self._get_prop('colormatrix_primaries')

    @colormatrix_primaries.setter
    def colormatrix_primaries(self, value):
        return self._set_prop('colormatrix_primaries', value)

    @property
    def xv_ck(self):
        return self._get_prop('xv_ck')

    @xv_ck.setter
    def xv_ck(self, value):
        return self._set_prop('xv_ck', value)

    @property
    def video_pan_x(self):
        return self._get_prop('video_pan_x')

    @video_pan_x.setter
    def video_pan_x(self, value):
        return self._set_prop('video_pan_x', value)

    @property
    def audio_exclusive(self):
        return self._get_prop('audio_exclusive')

    @audio_exclusive.setter
    def audio_exclusive(self, value):
        return self._set_prop('audio_exclusive', value)

    @property
    def gpu_api(self):
        return self._get_prop('gpu_api')

    @gpu_api.setter
    def gpu_api(self, value):
        return self._set_prop('gpu_api', value)

    @property
    def current_vo(self):
        return self._get_prop('current_vo')

    @current_vo.setter
    def current_vo(self, value):
        return self._set_prop('current_vo', value)

    @property
    def o(self):
        return self._get_prop('o')

    @o.setter
    def o(self, value):
        return self._set_prop('o', value)

    @property
    def sub_text_shadow_color(self):
        return self._get_prop('sub_text_shadow_color')

    @sub_text_shadow_color.setter
    def sub_text_shadow_color(self, value):
        return self._set_prop('sub_text_shadow_color', value)

    @property
    def sub_spacing(self):
        return self._get_prop('sub_spacing')

    @sub_spacing.setter
    def sub_spacing(self, value):
        return self._set_prop('sub_spacing', value)

    @property
    def tscale_radius(self):
        return self._get_prop('tscale_radius')

    @tscale_radius.setter
    def tscale_radius(self, value):
        return self._set_prop('tscale_radius', value)

    @property
    def mc(self):
        return self._get_prop('mc')

    @mc.setter
    def mc(self, value):
        return self._set_prop('mc', value)

    @property
    def paused_for_cache(self):
        return self._get_prop('paused_for_cache')

    @paused_for_cache.setter
    def paused_for_cache(self, value):
        return self._set_prop('paused_for_cache', value)

    @property
    def playlist_playing_pos(self):
        return self._get_prop('playlist_playing_pos')

    @playlist_playing_pos.setter
    def playlist_playing_pos(self, value):
        return self._set_prop('playlist_playing_pos', value)

    @property
    def xv_ck_method(self):
        return self._get_prop('xv_ck_method')

    @xv_ck_method.setter
    def xv_ck_method(self, value):
        return self._set_prop('xv_ck_method', value)

    @property
    def video_out_params(self):
        return self._get_prop('video_out_params')

    @video_out_params.setter
    def video_out_params(self, value):
        return self._set_prop('video_out_params', value)

    @property
    def opengl_sw(self):
        return self._get_prop('opengl_sw')

    @opengl_sw.setter
    def opengl_sw(self, value):
        return self._set_prop('opengl_sw', value)

    @property
    def duration(self):
        return self._get_prop('duration')

    @duration.setter
    def duration(self, value):
        return self._set_prop('duration', value)

    @property
    def ao_null_speed(self):
        return self._get_prop('ao_null_speed')

    @ao_null_speed.setter
    def ao_null_speed(self, value):
        return self._set_prop('ao_null_speed', value)

    @property
    def ocopy_metadata(self):
        return self._get_prop('ocopy_metadata')

    @ocopy_metadata.setter
    def ocopy_metadata(self, value):
        return self._set_prop('ocopy_metadata', value)

    @property
    def really_quiet(self):
        return self._get_prop('really_quiet')

    @really_quiet.setter
    def really_quiet(self, value):
        return self._set_prop('really_quiet', value)

    @property
    def time_pos(self):
        return self._get_prop('time_pos')

    @time_pos.setter
    def time_pos(self, value):
        return self._set_prop('time_pos', value)

    @property
    def dscale_param2(self):
        return self._get_prop('dscale_param2')

    @dscale_param2.setter
    def dscale_param2(self, value):
        return self._set_prop('dscale_param2', value)

    @property
    def osd_bar(self):
        return self._get_prop('osd_bar')

    @osd_bar.setter
    def osd_bar(self, value):
        return self._set_prop('osd_bar', value)

    @property
    def vo_vdpau_composite_detect(self):
        return self._get_prop('vo_vdpau_composite_detect')

    @vo_vdpau_composite_detect.setter
    def vo_vdpau_composite_detect(self, value):
        return self._set_prop('vo_vdpau_composite_detect', value)

    @property
    def osd_level(self):
        return self._get_prop('osd_level')

    @osd_level.setter
    def osd_level(self, value):
        return self._set_prop('osd_level', value)

    @property
    def referrer(self):
        return self._get_prop('referrer')

    @referrer.setter
    def referrer(self, value):
        return self._set_prop('referrer', value)

    @property
    def cover_art_auto(self):
        return self._get_prop('cover_art_auto')

    @cover_art_auto.setter
    def cover_art_auto(self, value):
        return self._set_prop('cover_art_auto', value)

    @property
    def subpos(self):
        return self._get_prop('subpos')

    @subpos.setter
    def subpos(self, value):
        return self._set_prop('subpos', value)

    @property
    def cscale_window(self):
        return self._get_prop('cscale_window')

    @cscale_window.setter
    def cscale_window(self, value):
        return self._set_prop('cscale_window', value)

    @property
    def http_proxy(self):
        return self._get_prop('http_proxy')

    @http_proxy.setter
    def http_proxy(self, value):
        return self._set_prop('http_proxy', value)

    @property
    def hwdec_codecs(self):
        return self._get_prop('hwdec_codecs')

    @hwdec_codecs.setter
    def hwdec_codecs(self, value):
        return self._set_prop('hwdec_codecs', value)

    @property
    def cdda_skip(self):
        return self._get_prop('cdda_skip')

    @cdda_skip.setter
    def cdda_skip(self, value):
        return self._set_prop('cdda_skip', value)

    @property
    def cdda_toc_offset(self):
        return self._get_prop('cdda_toc_offset')

    @cdda_toc_offset.setter
    def cdda_toc_offset(self, value):
        return self._set_prop('cdda_toc_offset', value)

    @property
    def screen(self):
        return self._get_prop('screen')

    @screen.setter
    def screen(self, value):
        return self._set_prop('screen', value)

    @property
    def ovfirst(self):
        return self._get_prop('ovfirst')

    @ovfirst.setter
    def ovfirst(self, value):
        return self._set_prop('ovfirst', value)

    @property
    def stop_playback_on_init_failure(self):
        return self._get_prop('stop_playback_on_init_failure')

    @stop_playback_on_init_failure.setter
    def stop_playback_on_init_failure(self, value):
        return self._set_prop('stop_playback_on_init_failure', value)

    @property
    def audio_wait_open(self):
        return self._get_prop('audio_wait_open')

    @audio_wait_open.setter
    def audio_wait_open(self, value):
        return self._set_prop('audio_wait_open', value)

    @property
    def replaygain_clip(self):
        return self._get_prop('replaygain_clip')

    @replaygain_clip.setter
    def replaygain_clip(self, value):
        return self._set_prop('replaygain_clip', value)

    @property
    def video_margin_ratio_left(self):
        return self._get_prop('video_margin_ratio_left')

    @video_margin_ratio_left.setter
    def video_margin_ratio_left(self, value):
        return self._set_prop('video_margin_ratio_left', value)

    @property
    def tls_key_file(self):
        return self._get_prop('tls_key_file')

    @tls_key_file.setter
    def tls_key_file(self, value):
        return self._set_prop('tls_key_file', value)

    @property
    def drop_frame_count(self):
        return self._get_prop('drop_frame_count')

    @drop_frame_count.setter
    def drop_frame_count(self, value):
        return self._set_prop('drop_frame_count', value)

    @property
    def audio_spdif(self):
        return self._get_prop('audio_spdif')

    @audio_spdif.setter
    def audio_spdif(self, value):
        return self._set_prop('audio_spdif', value)

    @property
    def stream_record(self):
        return self._get_prop('stream_record')

    @stream_record.setter
    def stream_record(self, value):
        return self._set_prop('stream_record', value)

    @property
    def gapless_audio(self):
        return self._get_prop('gapless_audio')

    @gapless_audio.setter
    def gapless_audio(self, value):
        return self._set_prop('gapless_audio', value)

    @property
    def framedrop(self):
        return self._get_prop('framedrop')

    @framedrop.setter
    def framedrop(self, value):
        return self._set_prop('framedrop', value)

    @property
    def display_fps(self):
        return self._get_prop('display_fps')

    @display_fps.setter
    def display_fps(self, value):
        return self._set_prop('display_fps', value)

    @property
    def screenshot_png_filter(self):
        return self._get_prop('screenshot_png_filter')

    @screenshot_png_filter.setter
    def screenshot_png_filter(self, value):
        return self._set_prop('screenshot_png_filter', value)

    @property
    def ytdl_raw_options(self):
        return self._get_prop('ytdl_raw_options')

    @ytdl_raw_options.setter
    def ytdl_raw_options(self, value):
        return self._set_prop('ytdl_raw_options', value)

    @property
    def gpu_hwdec_interop(self):
        return self._get_prop('gpu_hwdec_interop')

    @gpu_hwdec_interop.setter
    def gpu_hwdec_interop(self, value):
        return self._set_prop('gpu_hwdec_interop', value)

    @property
    def name(self):
        return self._get_prop('name')

    @name.setter
    def name(self, value):
        return self._set_prop('name', value)

    @property
    def video_timing_offset(self):
        return self._get_prop('video_timing_offset')

    @video_timing_offset.setter
    def video_timing_offset(self, value):
        return self._set_prop('video_timing_offset', value)

    @property
    def temporal_dither(self):
        return self._get_prop('temporal_dither')

    @temporal_dither.setter
    def temporal_dither(self, value):
        return self._set_prop('temporal_dither', value)

    @property
    def stream_end(self):
        return self._get_prop('stream_end')

    @stream_end.setter
    def stream_end(self, value):
        return self._set_prop('stream_end', value)

    @property
    def sub_end(self):
        return self._get_prop('sub_end')

    @sub_end.setter
    def sub_end(self, value):
        return self._set_prop('sub_end', value)

    @property
    def autosub_match(self):
        return self._get_prop('autosub_match')

    @autosub_match.setter
    def autosub_match(self, value):
        return self._set_prop('autosub_match', value)

    @property
    def taskbar_progress(self):
        return self._get_prop('taskbar_progress')

    @taskbar_progress.setter
    def taskbar_progress(self, value):
        return self._set_prop('taskbar_progress', value)

    @property
    def vo_vdpau_pullup(self):
        return self._get_prop('vo_vdpau_pullup')

    @vo_vdpau_pullup.setter
    def vo_vdpau_pullup(self, value):
        return self._set_prop('vo_vdpau_pullup', value)

    @property
    def sub_text_italic(self):
        return self._get_prop('sub_text_italic')

    @sub_text_italic.setter
    def sub_text_italic(self, value):
        return self._set_prop('sub_text_italic', value)

    @property
    def softvol_max(self):
        return self._get_prop('softvol_max')

    @softvol_max.setter
    def softvol_max(self, value):
        return self._set_prop('softvol_max', value)

    @property
    def sub_italic(self):
        return self._get_prop('sub_italic')

    @sub_italic.setter
    def sub_italic(self, value):
        return self._set_prop('sub_italic', value)

    @property
    def osd_on_seek(self):
        return self._get_prop('osd_on_seek')

    @osd_on_seek.setter
    def osd_on_seek(self, value):
        return self._set_prop('osd_on_seek', value)

    @property
    def opengl_vsync_fences(self):
        return self._get_prop('opengl_vsync_fences')

    @opengl_vsync_fences.setter
    def opengl_vsync_fences(self, value):
        return self._set_prop('opengl_vsync_fences', value)

    @property
    def vo_image_format(self):
        return self._get_prop('vo_image_format')

    @vo_image_format.setter
    def vo_image_format(self, value):
        return self._set_prop('vo_image_format', value)

    @property
    def cache_speed(self):
        return self._get_prop('cache_speed')

    @cache_speed.setter
    def cache_speed(self, value):
        return self._set_prop('cache_speed', value)

    @property
    def dvd_angle(self):
        return self._get_prop('dvd_angle')

    @dvd_angle.setter
    def dvd_angle(self, value):
        return self._set_prop('dvd_angle', value)

    @property
    def term_osd(self):
        return self._get_prop('term_osd')

    @term_osd.setter
    def term_osd(self, value):
        return self._set_prop('term_osd', value)

    @property
    def oset_metadata(self):
        return self._get_prop('oset_metadata')

    @oset_metadata.setter
    def oset_metadata(self, value):
        return self._set_prop('oset_metadata', value)

    @property
    def demuxer_cue_codepage(self):
        return self._get_prop('demuxer_cue_codepage')

    @demuxer_cue_codepage.setter
    def demuxer_cue_codepage(self, value):
        return self._set_prop('demuxer_cue_codepage', value)

    @property
    def sub_text_margin_x(self):
        return self._get_prop('sub_text_margin_x')

    @sub_text_margin_x.setter
    def sub_text_margin_x(self, value):
        return self._set_prop('sub_text_margin_x', value)

    @property
    def cuda_decode_device(self):
        return self._get_prop('cuda_decode_device')

    @cuda_decode_device.setter
    def cuda_decode_device(self, value):
        return self._set_prop('cuda_decode_device', value)

    @property
    def vd_lavc_threads(self):
        return self._get_prop('vd_lavc_threads')

    @vd_lavc_threads.setter
    def vd_lavc_threads(self, value):
        return self._set_prop('vd_lavc_threads', value)

    @property
    def osd_bar_h(self):
        return self._get_prop('osd_bar_h')

    @osd_bar_h.setter
    def osd_bar_h(self, value):
        return self._set_prop('osd_bar_h', value)

    @property
    def sub_align_y(self):
        return self._get_prop('sub_align_y')

    @sub_align_y.setter
    def sub_align_y(self, value):
        return self._set_prop('sub_align_y', value)

    @property
    def aid(self):
        return self._get_prop('aid')

    @aid.setter
    def aid(self, value):
        return self._set_prop('aid', value)

    @property
    def target_prim(self):
        return self._get_prop('target_prim')

    @target_prim.setter
    def target_prim(self, value):
        return self._set_prop('target_prim', value)

    @property
    def ass_scale_with_window(self):
        return self._get_prop('ass_scale_with_window')

    @ass_scale_with_window.setter
    def ass_scale_with_window(self, value):
        return self._set_prop('ass_scale_with_window', value)

    @property
    def icc_intent(self):
        return self._get_prop('icc_intent')

    @icc_intent.setter
    def icc_intent(self, value):
        return self._set_prop('icc_intent', value)

    @property
    def playtime_remaining(self):
        return self._get_prop('playtime_remaining')

    @playtime_remaining.setter
    def playtime_remaining(self, value):
        return self._set_prop('playtime_remaining', value)

    @property
    def gamma_factor(self):
        return self._get_prop('gamma_factor')

    @gamma_factor.setter
    def gamma_factor(self, value):
        return self._set_prop('gamma_factor', value)

    @property
    def ass(self):
        return self._get_prop('ass')

    @ass.setter
    def ass(self, value):
        return self._set_prop('ass', value)

    @property
    def demuxer_rawvideo_h(self):
        return self._get_prop('demuxer_rawvideo_h')

    @demuxer_rawvideo_h.setter
    def demuxer_rawvideo_h(self, value):
        return self._set_prop('demuxer_rawvideo_h', value)

    @property
    def panscan(self):
        return self._get_prop('panscan')

    @panscan.setter
    def panscan(self, value):
        return self._set_prop('panscan', value)

    @property
    def cache_pause_initial(self):
        return self._get_prop('cache_pause_initial')

    @cache_pause_initial.setter
    def cache_pause_initial(self, value):
        return self._set_prop('cache_pause_initial', value)

    @property
    def audio_out_params(self):
        return self._get_prop('audio_out_params')

    @audio_out_params.setter
    def audio_out_params(self, value):
        return self._set_prop('audio_out_params', value)

    @property
    def demuxer_lavf_linearize_timestamps(self):
        return self._get_prop('demuxer_lavf_linearize_timestamps')

    @demuxer_lavf_linearize_timestamps.setter
    def demuxer_lavf_linearize_timestamps(self, value):
        return self._set_prop('demuxer_lavf_linearize_timestamps', value)

    @property
    def wayland_edge_pixels_touch(self):
        return self._get_prop('wayland_edge_pixels_touch')

    @wayland_edge_pixels_touch.setter
    def wayland_edge_pixels_touch(self, value):
        return self._set_prop('wayland_edge_pixels_touch', value)

    @property
    def demuxer_termination_timeout(self):
        return self._get_prop('demuxer_termination_timeout')

    @demuxer_termination_timeout.setter
    def demuxer_termination_timeout(self, value):
        return self._set_prop('demuxer_termination_timeout', value)

    @property
    def audio_speed_correction(self):
        return self._get_prop('audio_speed_correction')

    @audio_speed_correction.setter
    def audio_speed_correction(self, value):
        return self._set_prop('audio_speed_correction', value)

    @property
    def dscale(self):
        return self._get_prop('dscale')

    @dscale.setter
    def dscale(self, value):
        return self._set_prop('dscale', value)

    @property
    def gpu_sw(self):
        return self._get_prop('gpu_sw')

    @gpu_sw.setter
    def gpu_sw(self, value):
        return self._set_prop('gpu_sw', value)

    @property
    def idle_active(self):
        return self._get_prop('idle_active')

    @idle_active.setter
    def idle_active(self, value):
        return self._set_prop('idle_active', value)

    @property
    def osd_font(self):
        return self._get_prop('osd_font')

    @osd_font.setter
    def osd_font(self, value):
        return self._set_prop('osd_font', value)

    @property
    def ab_loop_count(self):
        return self._get_prop('ab_loop_count')

    @ab_loop_count.setter
    def ab_loop_count(self, value):
        return self._set_prop('ab_loop_count', value)

    @property
    def audio_reversal_buffer(self):
        return self._get_prop('audio_reversal_buffer')

    @audio_reversal_buffer.setter
    def audio_reversal_buffer(self, value):
        return self._set_prop('audio_reversal_buffer', value)

    @property
    def sid(self):
        return self._get_prop('sid')

    @sid.setter
    def sid(self, value):
        return self._set_prop('sid', value)

    @property
    def sub_ass_scale_with_window(self):
        return self._get_prop('sub_ass_scale_with_window')

    @sub_ass_scale_with_window.setter
    def sub_ass_scale_with_window(self, value):
        return self._set_prop('sub_ass_scale_with_window', value)

    @property
    def drm_connector(self):
        return self._get_prop('drm_connector')

    @drm_connector.setter
    def drm_connector(self, value):
        return self._set_prop('drm_connector', value)

    @property
    def load_unsafe_playlists(self):
        return self._get_prop('load_unsafe_playlists')

    @load_unsafe_playlists.setter
    def load_unsafe_playlists(self, value):
        return self._set_prop('load_unsafe_playlists', value)

    @property
    def demuxer_rawvideo_size(self):
        return self._get_prop('demuxer_rawvideo_size')

    @demuxer_rawvideo_size.setter
    def demuxer_rawvideo_size(self, value):
        return self._set_prop('demuxer_rawvideo_size', value)

    @property
    def sws_bitexact(self):
        return self._get_prop('sws_bitexact')

    @sws_bitexact.setter
    def sws_bitexact(self, value):
        return self._set_prop('sws_bitexact', value)

    @property
    def tone_mapping_desaturate_exponent(self):
        return self._get_prop('tone_mapping_desaturate_exponent')

    @tone_mapping_desaturate_exponent.setter
    def tone_mapping_desaturate_exponent(self, value):
        return self._set_prop('tone_mapping_desaturate_exponent', value)

    @property
    def zimg_scaler_chroma(self):
        return self._get_prop('zimg_scaler_chroma')

    @zimg_scaler_chroma.setter
    def zimg_scaler_chroma(self, value):
        return self._set_prop('zimg_scaler_chroma', value)

    @property
    def screenshot_png_compression(self):
        return self._get_prop('screenshot_png_compression')

    @screenshot_png_compression.setter
    def screenshot_png_compression(self, value):
        return self._set_prop('screenshot_png_compression', value)

    @property
    def ad_lavc_o(self):
        return self._get_prop('ad_lavc_o')

    @ad_lavc_o.setter
    def ad_lavc_o(self, value):
        return self._set_prop('ad_lavc_o', value)

    @property
    def protocol_list(self):
        return self._get_prop('protocol_list')

    @protocol_list.setter
    def protocol_list(self, value):
        return self._set_prop('protocol_list', value)

    @property
    def subcp(self):
        return self._get_prop('subcp')

    @subcp.setter
    def subcp(self, value):
        return self._set_prop('subcp', value)

    @property
    def audio_delay(self):
        return self._get_prop('audio_delay')

    @audio_delay.setter
    def audio_delay(self, value):
        return self._set_prop('audio_delay', value)

    @property
    def vo_image_jpeg_source_chroma(self):
        return self._get_prop('vo_image_jpeg_source_chroma')

    @vo_image_jpeg_source_chroma.setter
    def vo_image_jpeg_source_chroma(self, value):
        return self._set_prop('vo_image_jpeg_source_chroma', value)

    @property
    def time_start(self):
        return self._get_prop('time_start')

    @time_start.setter
    def time_start(self, value):
        return self._set_prop('time_start', value)

    @property
    def sub_text_ass(self):
        return self._get_prop('sub_text_ass')

    @sub_text_ass.setter
    def sub_text_ass(self, value):
        return self._set_prop('sub_text_ass', value)

    @property
    def opengl_glfinish(self):
        return self._get_prop('opengl_glfinish')

    @opengl_glfinish.setter
    def opengl_glfinish(self, value):
        return self._set_prop('opengl_glfinish', value)

    @property
    def demuxer_thread(self):
        return self._get_prop('demuxer_thread')

    @demuxer_thread.setter
    def demuxer_thread(self, value):
        return self._set_prop('demuxer_thread', value)

    @property
    def opengl_dumb_mode(self):
        return self._get_prop('opengl_dumb_mode')

    @opengl_dumb_mode.setter
    def opengl_dumb_mode(self, value):
        return self._set_prop('opengl_dumb_mode', value)

    @property
    def script_opts(self):
        return self._get_prop('script_opts')

    @script_opts.setter
    def script_opts(self, value):
        return self._set_prop('script_opts', value)

    @property
    def sws_scaler(self):
        return self._get_prop('sws_scaler')

    @sws_scaler.setter
    def sws_scaler(self, value):
        return self._set_prop('sws_scaler', value)

    @property
    def ad_lavc_ac3drc(self):
        return self._get_prop('ad_lavc_ac3drc')

    @ad_lavc_ac3drc.setter
    def ad_lavc_ac3drc(self, value):
        return self._set_prop('ad_lavc_ac3drc', value)

    @property
    def ass_shaper(self):
        return self._get_prop('ass_shaper')

    @ass_shaper.setter
    def ass_shaper(self, value):
        return self._set_prop('ass_shaper', value)

    @property
    def osd(self):
        return self._get_prop('osd')

    @osd.setter
    def osd(self, value):
        return self._set_prop('osd', value)

    @property
    def options(self):
        return self._get_prop('options')

    @options.setter
    def options(self, value):
        return self._set_prop('options', value)

    @property
    def status_msg(self):
        return self._get_prop('status_msg')

    @status_msg.setter
    def status_msg(self, value):
        return self._set_prop('status_msg', value)

    @property
    def sub_ass_styles(self):
        return self._get_prop('sub_ass_styles')

    @sub_ass_styles.setter
    def sub_ass_styles(self, value):
        return self._set_prop('sub_ass_styles', value)

    @property
    def display_tags(self):
        return self._get_prop('display_tags')

    @display_tags.setter
    def display_tags(self, value):
        return self._set_prop('display_tags', value)

    @property
    def vd_lavc_fast(self):
        return self._get_prop('vd_lavc_fast')

    @vd_lavc_fast.setter
    def vd_lavc_fast(self, value):
        return self._set_prop('vd_lavc_fast', value)

    @property
    def contrast(self):
        return self._get_prop('contrast')

    @contrast.setter
    def contrast(self, value):
        return self._set_prop('contrast', value)

    @property
    def ao_null_latency(self):
        return self._get_prop('ao_null_latency')

    @ao_null_latency.setter
    def ao_null_latency(self, value):
        return self._set_prop('ao_null_latency', value)

    @property
    def ass_vsfilter_color_compat(self):
        return self._get_prop('ass_vsfilter_color_compat')

    @ass_vsfilter_color_compat.setter
    def ass_vsfilter_color_compat(self, value):
        return self._set_prop('ass_vsfilter_color_compat', value)

    @property
    def property_list(self):
        return self._get_prop('property_list')

    @property_list.setter
    def property_list(self, value):
        return self._set_prop('property_list', value)

    @property
    def demuxer_rawvideo_fps(self):
        return self._get_prop('demuxer_rawvideo_fps')

    @demuxer_rawvideo_fps.setter
    def demuxer_rawvideo_fps(self, value):
        return self._set_prop('demuxer_rawvideo_fps', value)

    @property
    def tone_mapping_max_boost(self):
        return self._get_prop('tone_mapping_max_boost')

    @tone_mapping_max_boost.setter
    def tone_mapping_max_boost(self, value):
        return self._set_prop('tone_mapping_max_boost', value)

    @property
    def border(self):
        return self._get_prop('border')

    @border.setter
    def border(self, value):
        return self._set_prop('border', value)

    @property
    def total_avsync_change(self):
        return self._get_prop('total_avsync_change')

    @total_avsync_change.setter
    def total_avsync_change(self, value):
        return self._set_prop('total_avsync_change', value)

    @property
    def sigmoid_upscaling(self):
        return self._get_prop('sigmoid_upscaling')

    @sigmoid_upscaling.setter
    def sigmoid_upscaling(self, value):
        return self._set_prop('sigmoid_upscaling', value)

    @property
    def zimg_threads(self):
        return self._get_prop('zimg_threads')

    @zimg_threads.setter
    def zimg_threads(self, value):
        return self._set_prop('zimg_threads', value)

    @property
    def cache_unlink_files(self):
        return self._get_prop('cache_unlink_files')

    @cache_unlink_files.setter
    def cache_unlink_files(self, value):
        return self._set_prop('cache_unlink_files', value)

    @property
    def dheight(self):
        return self._get_prop('dheight')

    @dheight.setter
    def dheight(self, value):
        return self._set_prop('dheight', value)

    @property
    def dscale_wtaper(self):
        return self._get_prop('dscale_wtaper')

    @dscale_wtaper.setter
    def dscale_wtaper(self, value):
        return self._set_prop('dscale_wtaper', value)

    @property
    def audio_resample_phase_shift(self):
        return self._get_prop('audio_resample_phase_shift')

    @audio_resample_phase_shift.setter
    def audio_resample_phase_shift(self, value):
        return self._set_prop('audio_resample_phase_shift', value)

    @property
    def osd_color(self):
        return self._get_prop('osd_color')

    @osd_color.setter
    def osd_color(self, value):
        return self._set_prop('osd_color', value)

    @property
    def icc_cache_dir(self):
        return self._get_prop('icc_cache_dir')

    @icc_cache_dir.setter
    def icc_cache_dir(self, value):
        return self._set_prop('icc_cache_dir', value)

    @property
    def oaoffset(self):
        return self._get_prop('oaoffset')

    @oaoffset.setter
    def oaoffset(self, value):
        return self._set_prop('oaoffset', value)

    @property
    def oafirst(self):
        return self._get_prop('oafirst')

    @oafirst.setter
    def oafirst(self, value):
        return self._set_prop('oafirst', value)

    @property
    def sstep(self):
        return self._get_prop('sstep')

    @sstep.setter
    def sstep(self, value):
        return self._set_prop('sstep', value)

    @property
    def gamut_clipping(self):
        return self._get_prop('gamut_clipping')

    @gamut_clipping.setter
    def gamut_clipping(self, value):
        return self._set_prop('gamut_clipping', value)

    @property
    def sub_shadow_color(self):
        return self._get_prop('sub_shadow_color')

    @sub_shadow_color.setter
    def sub_shadow_color(self, value):
        return self._set_prop('sub_shadow_color', value)

    @property
    def drm_draw_surface_size(self):
        return self._get_prop('drm_draw_surface_size')

    @drm_draw_surface_size.setter
    def drm_draw_surface_size(self, value):
        return self._set_prop('drm_draw_surface_size', value)

    @property
    def sub_scale_by_window(self):
        return self._get_prop('sub_scale_by_window')

    @sub_scale_by_window.setter
    def sub_scale_by_window(self, value):
        return self._set_prop('sub_scale_by_window', value)

    @property
    def core_idle(self):
        return self._get_prop('core_idle')

    @core_idle.setter
    def core_idle(self, value):
        return self._set_prop('core_idle', value)

    @property
    def chapter_seek_threshold(self):
        return self._get_prop('chapter_seek_threshold')

    @chapter_seek_threshold.setter
    def chapter_seek_threshold(self, value):
        return self._set_prop('chapter_seek_threshold', value)

    @property
    def dither_depth(self):
        return self._get_prop('dither_depth')

    @dither_depth.setter
    def dither_depth(self, value):
        return self._set_prop('dither_depth', value)

    @property
    def gamma_auto(self):
        return self._get_prop('gamma_auto')

    @gamma_auto.setter
    def gamma_auto(self, value):
        return self._set_prop('gamma_auto', value)

    @property
    def video_speed_correction(self):
        return self._get_prop('video_speed_correction')

    @video_speed_correction.setter
    def video_speed_correction(self, value):
        return self._set_prop('video_speed_correction', value)

    @property
    def zimg_scaler_chroma_param_b(self):
        return self._get_prop('zimg_scaler_chroma_param_b')

    @zimg_scaler_chroma_param_b.setter
    def zimg_scaler_chroma_param_b(self, value):
        return self._set_prop('zimg_scaler_chroma_param_b', value)

    @property
    def scale_clamp(self):
        return self._get_prop('scale_clamp')

    @scale_clamp.setter
    def scale_clamp(self, value):
        return self._set_prop('scale_clamp', value)

    @property
    def keep_open(self):
        return self._get_prop('keep_open')

    @keep_open.setter
    def keep_open(self, value):
        return self._set_prop('keep_open', value)

    @property
    def background(self):
        return self._get_prop('background')

    @background.setter
    def background(self, value):
        return self._set_prop('background', value)

    @property
    def sub_fuzziness(self):
        return self._get_prop('sub_fuzziness')

    @sub_fuzziness.setter
    def sub_fuzziness(self, value):
        return self._set_prop('sub_fuzziness', value)

    @property
    def cscale_cutoff(self):
        return self._get_prop('cscale_cutoff')

    @cscale_cutoff.setter
    def cscale_cutoff(self, value):
        return self._set_prop('cscale_cutoff', value)

    @property
    def sub_gauss(self):
        return self._get_prop('sub_gauss')

    @sub_gauss.setter
    def sub_gauss(self, value):
        return self._set_prop('sub_gauss', value)

    @property
    def screenshot_webp_quality(self):
        return self._get_prop('screenshot_webp_quality')

    @screenshot_webp_quality.setter
    def screenshot_webp_quality(self, value):
        return self._set_prop('screenshot_webp_quality', value)

    @property
    def drm_draw_plane(self):
        return self._get_prop('drm_draw_plane')

    @drm_draw_plane.setter
    def drm_draw_plane(self, value):
        return self._set_prop('drm_draw_plane', value)

    @property
    def ss(self):
        return self._get_prop('ss')

    @ss.setter
    def ss(self, value):
        return self._set_prop('ss', value)

    @property
    def video_params(self):
        return self._get_prop('video_params')

    @video_params.setter
    def video_params(self, value):
        return self._set_prop('video_params', value)

    @property
    def cache_pause(self):
        return self._get_prop('cache_pause')

    @cache_pause.setter
    def cache_pause(self, value):
        return self._set_prop('cache_pause', value)

    @property
    def osd_status_msg(self):
        return self._get_prop('osd_status_msg')

    @osd_status_msg.setter
    def osd_status_msg(self, value):
        return self._set_prop('osd_status_msg', value)

    @property
    def demuxer_lavf_probesize(self):
        return self._get_prop('demuxer_lavf_probesize')

    @demuxer_lavf_probesize.setter
    def demuxer_lavf_probesize(self, value):
        return self._set_prop('demuxer_lavf_probesize', value)

    @property
    def rtsp_transport(self):
        return self._get_prop('rtsp_transport')

    @rtsp_transport.setter
    def rtsp_transport(self, value):
        return self._set_prop('rtsp_transport', value)

    @property
    def vo_drop_frame_count(self):
        return self._get_prop('vo_drop_frame_count')

    @vo_drop_frame_count.setter
    def vo_drop_frame_count(self, value):
        return self._set_prop('vo_drop_frame_count', value)

    @property
    def sub_ass_vsfilter_color_compat(self):
        return self._get_prop('sub_ass_vsfilter_color_compat')

    @sub_ass_vsfilter_color_compat.setter
    def sub_ass_vsfilter_color_compat(self, value):
        return self._set_prop('sub_ass_vsfilter_color_compat', value)

    @property
    def audio_pitch_correction(self):
        return self._get_prop('audio_pitch_correction')

    @audio_pitch_correction.setter
    def audio_pitch_correction(self, value):
        return self._set_prop('audio_pitch_correction', value)

    @property
    def mixer_active(self):
        return self._get_prop('mixer_active')

    @mixer_active.setter
    def mixer_active(self, value):
        return self._set_prop('mixer_active', value)

    @property
    def overlay_ids(self):
        return self._get_prop('overlay_ids')

    @overlay_ids.setter
    def overlay_ids(self, value):
        return self._set_prop('overlay_ids', value)

    @property
    def sub_scale(self):
        return self._get_prop('sub_scale')

    @sub_scale.setter
    def sub_scale(self, value):
        return self._set_prop('sub_scale', value)

    @property
    def speed(self):
        return self._get_prop('speed')

    @speed.setter
    def speed(self, value):
        return self._set_prop('speed', value)

    @property
    def tscale_clamp(self):
        return self._get_prop('tscale_clamp')

    @tscale_clamp.setter
    def tscale_clamp(self, value):
        return self._set_prop('tscale_clamp', value)

    @property
    def vo_tct_algo(self):
        return self._get_prop('vo_tct_algo')

    @vo_tct_algo.setter
    def vo_tct_algo(self, value):
        return self._set_prop('vo_tct_algo', value)

    @property
    def cdda_span_b(self):
        return self._get_prop('cdda_span_b')

    @cdda_span_b.setter
    def cdda_span_b(self, value):
        return self._set_prop('cdda_span_b', value)

    @property
    def vo_vdpau_queuetime_fs(self):
        return self._get_prop('vo_vdpau_queuetime_fs')

    @vo_vdpau_queuetime_fs.setter
    def vo_vdpau_queuetime_fs(self, value):
        return self._set_prop('vo_vdpau_queuetime_fs', value)

    @property
    def term_status_msg(self):
        return self._get_prop('term_status_msg')

    @term_status_msg.setter
    def term_status_msg(self, value):
        return self._set_prop('term_status_msg', value)

    @property
    def libass_version(self):
        return self._get_prop('libass_version')

    @libass_version.setter
    def libass_version(self, value):
        return self._set_prop('libass_version', value)

    @property
    def input_ar_delay(self):
        return self._get_prop('input_ar_delay')

    @input_ar_delay.setter
    def input_ar_delay(self, value):
        return self._set_prop('input_ar_delay', value)

    @property
    def frames(self):
        return self._get_prop('frames')

    @frames.setter
    def frames(self, value):
        return self._set_prop('frames', value)

    @property
    def snap_window(self):
        return self._get_prop('snap_window')

    @snap_window.setter
    def snap_window(self, value):
        return self._set_prop('snap_window', value)

    @property
    def delay(self):
        return self._get_prop('delay')

    @delay.setter
    def delay(self, value):
        return self._set_prop('delay', value)

    @property
    def vo_image_outdir(self):
        return self._get_prop('vo_image_outdir')

    @vo_image_outdir.setter
    def vo_image_outdir(self, value):
        return self._set_prop('vo_image_outdir', value)

    @property
    def sub_text_blur(self):
        return self._get_prop('sub_text_blur')

    @sub_text_blur.setter
    def sub_text_blur(self, value):
        return self._set_prop('sub_text_blur', value)

    @property
    def sub_margin_x(self):
        return self._get_prop('sub_margin_x')

    @sub_margin_x.setter
    def sub_margin_x(self, value):
        return self._set_prop('sub_margin_x', value)

    @property
    def sub_justify(self):
        return self._get_prop('sub_justify')

    @sub_justify.setter
    def sub_justify(self, value):
        return self._set_prop('sub_justify', value)

    @property
    def opengl_swapinterval(self):
        return self._get_prop('opengl_swapinterval')

    @opengl_swapinterval.setter
    def opengl_swapinterval(self, value):
        return self._set_prop('opengl_swapinterval', value)

    @property
    def save_position_on_quit(self):
        return self._get_prop('save_position_on_quit')

    @save_position_on_quit.setter
    def save_position_on_quit(self, value):
        return self._set_prop('save_position_on_quit', value)

    @property
    def ass_styles(self):
        return self._get_prop('ass_styles')

    @ass_styles.setter
    def ass_styles(self, value):
        return self._set_prop('ass_styles', value)

    @property
    def input_ar_rate(self):
        return self._get_prop('input_ar_rate')

    @input_ar_rate.setter
    def input_ar_rate(self, value):
        return self._set_prop('input_ar_rate', value)

    @property
    def estimated_display_fps(self):
        return self._get_prop('estimated_display_fps')

    @estimated_display_fps.setter
    def estimated_display_fps(self, value):
        return self._set_prop('estimated_display_fps', value)

    @property
    def osd_bar_w(self):
        return self._get_prop('osd_bar_w')

    @osd_bar_w.setter
    def osd_bar_w(self, value):
        return self._set_prop('osd_bar_w', value)

    @property
    def video_dec_params(self):
        return self._get_prop('video_dec_params')

    @video_dec_params.setter
    def video_dec_params(self, value):
        return self._set_prop('video_dec_params', value)

    @property
    def input_ipc_client(self):
        return self._get_prop('input_ipc_client')

    @input_ipc_client.setter
    def input_ipc_client(self, value):
        return self._set_prop('input_ipc_client', value)

    @property
    def alsa_resample(self):
        return self._get_prop('alsa_resample')

    @alsa_resample.setter
    def alsa_resample(self, value):
        return self._set_prop('alsa_resample', value)

    @property
    def screenshot_webp_compression(self):
        return self._get_prop('screenshot_webp_compression')

    @screenshot_webp_compression.setter
    def screenshot_webp_compression(self, value):
        return self._set_prop('screenshot_webp_compression', value)

    @property
    def scale_param1(self):
        return self._get_prop('scale_param1')

    @scale_param1.setter
    def scale_param1(self, value):
        return self._set_prop('scale_param1', value)

    @property
    def title(self):
        return self._get_prop('title')

    @title.setter
    def title(self, value):
        return self._set_prop('title', value)

    @property
    def sub_file_paths(self):
        return self._get_prop('sub_file_paths')

    @sub_file_paths.setter
    def sub_file_paths(self, value):
        return self._set_prop('sub_file_paths', value)

    @property
    def volume(self):
        return self._get_prop('volume')

    @volume.setter
    def volume(self, value):
        return self._set_prop('volume', value)

    @property
    def sub_text_spacing(self):
        return self._get_prop('sub_text_spacing')

    @sub_text_spacing.setter
    def sub_text_spacing(self, value):
        return self._set_prop('sub_text_spacing', value)

    @property
    def ovcopts(self):
        return self._get_prop('ovcopts')

    @ovcopts.setter
    def ovcopts(self, value):
        return self._set_prop('ovcopts', value)

    @property
    def fps(self):
        return self._get_prop('fps')

    @fps.setter
    def fps(self, value):
        return self._set_prop('fps', value)

    @property
    def bluray_device(self):
        return self._get_prop('bluray_device')

    @bluray_device.setter
    def bluray_device(self, value):
        return self._set_prop('bluray_device', value)

    @property
    def input_bindings(self):
        return self._get_prop('input_bindings')

    @input_bindings.setter
    def input_bindings(self, value):
        return self._set_prop('input_bindings', value)

    @property
    def drm_drmprime_video_plane(self):
        return self._get_prop('drm_drmprime_video_plane')

    @drm_drmprime_video_plane.setter
    def drm_drmprime_video_plane(self, value):
        return self._set_prop('drm_drmprime_video_plane', value)

    @property
    def seekable(self):
        return self._get_prop('seekable')

    @seekable.setter
    def seekable(self, value):
        return self._set_prop('seekable', value)

    @property
    def config_dir(self):
        return self._get_prop('config_dir')

    @config_dir.setter
    def config_dir(self, value):
        return self._set_prop('config_dir', value)

    @property
    def sub_text_color(self):
        return self._get_prop('sub_text_color')

    @sub_text_color.setter
    def sub_text_color(self, value):
        return self._set_prop('sub_text_color', value)

    @property
    def focus_on_open(self):
        return self._get_prop('focus_on_open')

    @focus_on_open.setter
    def focus_on_open(self, value):
        return self._set_prop('focus_on_open', value)

    @property
    def use_embedded_icc_profile(self):
        return self._get_prop('use_embedded_icc_profile')

    @use_embedded_icc_profile.setter
    def use_embedded_icc_profile(self, value):
        return self._set_prop('use_embedded_icc_profile', value)

    @property
    def zimg_scaler_param_a(self):
        return self._get_prop('zimg_scaler_param_a')

    @zimg_scaler_param_a.setter
    def zimg_scaler_param_a(self, value):
        return self._set_prop('zimg_scaler_param_a', value)

    @property
    def cscale_wblur(self):
        return self._get_prop('cscale_wblur')

    @cscale_wblur.setter
    def cscale_wblur(self, value):
        return self._set_prop('cscale_wblur', value)

    @property
    def cdda_speed(self):
        return self._get_prop('cdda_speed')

    @cdda_speed.setter
    def cdda_speed(self, value):
        return self._set_prop('cdda_speed', value)

    @property
    def sub_fix_timing(self):
        return self._get_prop('sub_fix_timing')

    @sub_fix_timing.setter
    def sub_fix_timing(self, value):
        return self._set_prop('sub_fix_timing', value)

    @property
    def merge_files(self):
        return self._get_prop('merge_files')

    @merge_files.setter
    def merge_files(self, value):
        return self._set_prop('merge_files', value)

    @property
    def frame_drop_count(self):
        return self._get_prop('frame_drop_count')

    @frame_drop_count.setter
    def frame_drop_count(self, value):
        return self._set_prop('frame_drop_count', value)

    @property
    def record_file(self):
        return self._get_prop('record_file')

    @record_file.setter
    def record_file(self, value):
        return self._set_prop('record_file', value)

    @property
    def stream_pos(self):
        return self._get_prop('stream_pos')

    @stream_pos.setter
    def stream_pos(self, value):
        return self._set_prop('stream_pos', value)

    @property
    def video_pan_y(self):
        return self._get_prop('video_pan_y')

    @video_pan_y.setter
    def video_pan_y(self, value):
        return self._set_prop('video_pan_y', value)

    @property
    def hue(self):
        return self._get_prop('hue')

    @hue.setter
    def hue(self, value):
        return self._set_prop('hue', value)

    @property
    def vo_vdpau_fps(self):
        return self._get_prop('vo_vdpau_fps')

    @vo_vdpau_fps.setter
    def vo_vdpau_fps(self, value):
        return self._set_prop('vo_vdpau_fps', value)

    @property
    def encoder_list(self):
        return self._get_prop('encoder_list')

    @encoder_list.setter
    def encoder_list(self, value):
        return self._set_prop('encoder_list', value)

    @property
    def linear_downscaling(self):
        return self._get_prop('linear_downscaling')

    @linear_downscaling.setter
    def linear_downscaling(self, value):
        return self._set_prop('linear_downscaling', value)

    @property
    def sub_text_shadow_offset(self):
        return self._get_prop('sub_text_shadow_offset')

    @sub_text_shadow_offset.setter
    def sub_text_shadow_offset(self, value):
        return self._set_prop('sub_text_shadow_offset', value)

    @property
    def audio_buffer(self):
        return self._get_prop('audio_buffer')

    @audio_buffer.setter
    def audio_buffer(self, value):
        return self._set_prop('audio_buffer', value)

    @property
    def input_cursor(self):
        return self._get_prop('input_cursor')

    @input_cursor.setter
    def input_cursor(self, value):
        return self._set_prop('input_cursor', value)

    @property
    def osd_msg2(self):
        return self._get_prop('osd_msg2')

    @osd_msg2.setter
    def osd_msg2(self, value):
        return self._set_prop('osd_msg2', value)

    @property
    def cscale_antiring(self):
        return self._get_prop('cscale_antiring')

    @cscale_antiring.setter
    def cscale_antiring(self, value):
        return self._set_prop('cscale_antiring', value)

    @property
    def vd_lavc_assume_old_x264(self):
        return self._get_prop('vd_lavc_assume_old_x264')

    @vd_lavc_assume_old_x264.setter
    def vd_lavc_assume_old_x264(self, value):
        return self._set_prop('vd_lavc_assume_old_x264', value)

    @property
    def ordered_chapters_files(self):
        return self._get_prop('ordered_chapters_files')

    @ordered_chapters_files.setter
    def ordered_chapters_files(self, value):
        return self._set_prop('ordered_chapters_files', value)

    @property
    def scale_wparam(self):
        return self._get_prop('scale_wparam')

    @scale_wparam.setter
    def scale_wparam(self, value):
        return self._set_prop('scale_wparam', value)

    @property
    def video_sync_max_factor(self):
        return self._get_prop('video_sync_max_factor')

    @video_sync_max_factor.setter
    def video_sync_max_factor(self, value):
        return self._set_prop('video_sync_max_factor', value)

    @property
    def focused(self):
        return self._get_prop('focused')

    @focused.setter
    def focused(self, value):
        return self._set_prop('focused', value)

    @property
    def ordered_chapters(self):
        return self._get_prop('ordered_chapters')

    @ordered_chapters.setter
    def ordered_chapters(self, value):
        return self._set_prop('ordered_chapters', value)

    @property
    def chapter_merge_threshold(self):
        return self._get_prop('chapter_merge_threshold')

    @chapter_merge_threshold.setter
    def chapter_merge_threshold(self, value):
        return self._set_prop('chapter_merge_threshold', value)

    @property
    def sub_ass_vsfilter_aspect_compat(self):
        return self._get_prop('sub_ass_vsfilter_aspect_compat')

    @sub_ass_vsfilter_aspect_compat.setter
    def sub_ass_vsfilter_aspect_compat(self, value):
        return self._set_prop('sub_ass_vsfilter_aspect_compat', value)

    @property
    def term_playing_msg(self):
        return self._get_prop('term_playing_msg')

    @term_playing_msg.setter
    def term_playing_msg(self, value):
        return self._set_prop('term_playing_msg', value)

    @property
    def ass_vsfilter_blur_compat(self):
        return self._get_prop('ass_vsfilter_blur_compat')

    @ass_vsfilter_blur_compat.setter
    def ass_vsfilter_blur_compat(self, value):
        return self._set_prop('ass_vsfilter_blur_compat', value)

    @property
    def demuxer_mkv_subtitle_preroll_secs(self):
        return self._get_prop('demuxer_mkv_subtitle_preroll_secs')

    @demuxer_mkv_subtitle_preroll_secs.setter
    def demuxer_mkv_subtitle_preroll_secs(self, value):
        return self._set_prop('demuxer_mkv_subtitle_preroll_secs', value)

    @property
    def scaler_resizes_only(self):
        return self._get_prop('scaler_resizes_only')

    @scaler_resizes_only.setter
    def scaler_resizes_only(self, value):
        return self._set_prop('scaler_resizes_only', value)

    @property
    def sub_text_border_size(self):
        return self._get_prop('sub_text_border_size')

    @sub_text_border_size.setter
    def sub_text_border_size(self, value):
        return self._set_prop('sub_text_border_size', value)

    @property
    def dwidth(self):
        return self._get_prop('dwidth')

    @dwidth.setter
    def dwidth(self, value):
        return self._set_prop('dwidth', value)

    @property
    def hls_bitrate(self):
        return self._get_prop('hls_bitrate')

    @hls_bitrate.setter
    def hls_bitrate(self, value):
        return self._set_prop('hls_bitrate', value)

    @property
    def sws_ls(self):
        return self._get_prop('sws_ls')

    @sws_ls.setter
    def sws_ls(self, value):
        return self._set_prop('sws_ls', value)

    @property
    def cookies(self):
        return self._get_prop('cookies')

    @cookies.setter
    def cookies(self, value):
        return self._set_prop('cookies', value)

    @property
    def idx(self):
        return self._get_prop('idx')

    @idx.setter
    def idx(self, value):
        return self._set_prop('idx', value)

    @property
    def sub_delay(self):
        return self._get_prop('sub_delay')

    @sub_delay.setter
    def sub_delay(self, value):
        return self._set_prop('sub_delay', value)

    @property
    def ignore_path_in_watch_later_config(self):
        return self._get_prop('ignore_path_in_watch_later_config')

    @ignore_path_in_watch_later_config.setter
    def ignore_path_in_watch_later_config(self, value):
        return self._set_prop('ignore_path_in_watch_later_config', value)

    @property
    def blend_subtitles(self):
        return self._get_prop('blend_subtitles')

    @blend_subtitles.setter
    def blend_subtitles(self, value):
        return self._set_prop('blend_subtitles', value)

    @property
    def af(self):
        return self._get_prop('af')

    @af.setter
    def af(self, value):
        return self._set_prop('af', value)

    @property
    def sub_codepage(self):
        return self._get_prop('sub_codepage')

    @sub_codepage.setter
    def sub_codepage(self, value):
        return self._set_prop('sub_codepage', value)

    @property
    def native_keyrepeat(self):
        return self._get_prop('native_keyrepeat')

    @native_keyrepeat.setter
    def native_keyrepeat(self, value):
        return self._set_prop('native_keyrepeat', value)

    @property
    def dscale_radius(self):
        return self._get_prop('dscale_radius')

    @dscale_radius.setter
    def dscale_radius(self, value):
        return self._set_prop('dscale_radius', value)

    @property
    def cursor_autohide_fs_only(self):
        return self._get_prop('cursor_autohide_fs_only')

    @cursor_autohide_fs_only.setter
    def cursor_autohide_fs_only(self, value):
        return self._set_prop('cursor_autohide_fs_only', value)

    @property
    def autofit_larger(self):
        return self._get_prop('autofit_larger')

    @autofit_larger.setter
    def autofit_larger(self, value):
        return self._set_prop('autofit_larger', value)

    @property
    def keepaspect_window(self):
        return self._get_prop('keepaspect_window')

    @keepaspect_window.setter
    def keepaspect_window(self, value):
        return self._set_prop('keepaspect_window', value)

    @property
    def mf_fps(self):
        return self._get_prop('mf_fps')

    @mf_fps.setter
    def mf_fps(self, value):
        return self._set_prop('mf_fps', value)

    @property
    def osd_msg1(self):
        return self._get_prop('osd_msg1')

    @osd_msg1.setter
    def osd_msg1(self, value):
        return self._set_prop('osd_msg1', value)

    @property
    def editions(self):
        return self._get_prop('editions')

    @editions.setter
    def editions(self, value):
        return self._set_prop('editions', value)

    @property
    def osd_shadow_color(self):
        return self._get_prop('osd_shadow_color')

    @osd_shadow_color.setter
    def osd_shadow_color(self, value):
        return self._set_prop('osd_shadow_color', value)

    @property
    def srate(self):
        return self._get_prop('srate')

    @srate.setter
    def srate(self, value):
        return self._set_prop('srate', value)

    @property
    def deband_grain(self):
        return self._get_prop('deband_grain')

    @deband_grain.setter
    def deband_grain(self, value):
        return self._set_prop('deband_grain', value)

    @property
    def stop_screensaver(self):
        return self._get_prop('stop_screensaver')

    @stop_screensaver.setter
    def stop_screensaver(self, value):
        return self._set_prop('stop_screensaver', value)

    @property
    def hdr_compute_peak(self):
        return self._get_prop('hdr_compute_peak')

    @hdr_compute_peak.setter
    def hdr_compute_peak(self, value):
        return self._set_prop('hdr_compute_peak', value)

    @property
    def ad_queue_enable(self):
        return self._get_prop('ad_queue_enable')

    @ad_queue_enable.setter
    def ad_queue_enable(self, value):
        return self._set_prop('ad_queue_enable', value)

    @property
    def current_tracks(self):
        return self._get_prop('current_tracks')

    @current_tracks.setter
    def current_tracks(self, value):
        return self._set_prop('current_tracks', value)

    @property
    def sub_ass_line_spacing(self):
        return self._get_prop('sub_ass_line_spacing')

    @sub_ass_line_spacing.setter
    def sub_ass_line_spacing(self, value):
        return self._set_prop('sub_ass_line_spacing', value)

    @property
    def demuxer_cache_time(self):
        return self._get_prop('demuxer_cache_time')

    @demuxer_cache_time.setter
    def demuxer_cache_time(self, value):
        return self._set_prop('demuxer_cache_time', value)

    @property
    def untimed(self):
        return self._get_prop('untimed')

    @untimed.setter
    def untimed(self, value):
        return self._set_prop('untimed', value)

    @property
    def video_sync_max_video_change(self):
        return self._get_prop('video_sync_max_video_change')

    @video_sync_max_video_change.setter
    def video_sync_max_video_change(self, value):
        return self._set_prop('video_sync_max_video_change', value)

    @property
    def playlist(self):
        return self._get_prop('playlist')

    @playlist.setter
    def playlist(self, value):
        return self._set_prop('playlist', value)

    @property
    def terminal(self):
        return self._get_prop('terminal')

    @terminal.setter
    def terminal(self, value):
        return self._set_prop('terminal', value)

    @property
    def screenshot_high_bit_depth(self):
        return self._get_prop('screenshot_high_bit_depth')

    @screenshot_high_bit_depth.setter
    def screenshot_high_bit_depth(self, value):
        return self._set_prop('screenshot_high_bit_depth', value)

    @property
    def hwdec_current(self):
        return self._get_prop('hwdec_current')

    @hwdec_current.setter
    def hwdec_current(self, value):
        return self._set_prop('hwdec_current', value)

    @property
    def osd_ass_cc(self):
        return self._get_prop('osd_ass_cc')

    @osd_ass_cc.setter
    def osd_ass_cc(self, value):
        return self._set_prop('osd_ass_cc', value)

    @property
    def osd_shadow_offset(self):
        return self._get_prop('osd_shadow_offset')

    @osd_shadow_offset.setter
    def osd_shadow_offset(self, value):
        return self._set_prop('osd_shadow_offset', value)

    @property
    def input_right_alt_gr(self):
        return self._get_prop('input_right_alt_gr')

    @input_right_alt_gr.setter
    def input_right_alt_gr(self, value):
        return self._set_prop('input_right_alt_gr', value)

    @property
    def lavfi_complex(self):
        return self._get_prop('lavfi_complex')

    @lavfi_complex.setter
    def lavfi_complex(self, value):
        return self._set_prop('lavfi_complex', value)

    @property
    def replaygain_fallback(self):
        return self._get_prop('replaygain_fallback')

    @replaygain_fallback.setter
    def replaygain_fallback(self, value):
        return self._set_prop('replaygain_fallback', value)

    @property
    def sub_ass_override(self):
        return self._get_prop('sub_ass_override')

    @sub_ass_override.setter
    def sub_ass_override(self, value):
        return self._set_prop('sub_ass_override', value)

    @property
    def vd_lavc_o(self):
        return self._get_prop('vd_lavc_o')

    @vd_lavc_o.setter
    def vd_lavc_o(self, value):
        return self._set_prop('vd_lavc_o', value)

    @property
    def demuxer_mkv_subtitle_preroll(self):
        return self._get_prop('demuxer_mkv_subtitle_preroll')

    @demuxer_mkv_subtitle_preroll.setter
    def demuxer_mkv_subtitle_preroll(self, value):
        return self._set_prop('demuxer_mkv_subtitle_preroll', value)

    @property
    def cscale_param2(self):
        return self._get_prop('cscale_param2')

    @cscale_param2.setter
    def cscale_param2(self, value):
        return self._set_prop('cscale_param2', value)

    @property
    def dscale_antiring(self):
        return self._get_prop('dscale_antiring')

    @dscale_antiring.setter
    def dscale_antiring(self, value):
        return self._set_prop('dscale_antiring', value)

    @property
    def cdda_toc_bias(self):
        return self._get_prop('cdda_toc_bias')

    @cdda_toc_bias.setter
    def cdda_toc_bias(self, value):
        return self._set_prop('cdda_toc_bias', value)

    @property
    def resume_playback_check_mtime(self):
        return self._get_prop('resume_playback_check_mtime')

    @resume_playback_check_mtime.setter
    def resume_playback_check_mtime(self, value):
        return self._set_prop('resume_playback_check_mtime', value)

    @property
    def deinterlace(self):
        return self._get_prop('deinterlace')

    @deinterlace.setter
    def deinterlace(self, value):
        return self._set_prop('deinterlace', value)

    @property
    def dvbin_card(self):
        return self._get_prop('dvbin_card')

    @dvbin_card.setter
    def dvbin_card(self, value):
        return self._set_prop('dvbin_card', value)

    @property
    def alsa_mixer_name(self):
        return self._get_prop('alsa_mixer_name')

    @alsa_mixer_name.setter
    def alsa_mixer_name(self, value):
        return self._set_prop('alsa_mixer_name', value)

    @property
    def subfont_text_scale(self):
        return self._get_prop('subfont_text_scale')

    @subfont_text_scale.setter
    def subfont_text_scale(self, value):
        return self._set_prop('subfont_text_scale', value)

    @property
    def command_list(self):
        return self._get_prop('command_list')

    @command_list.setter
    def command_list(self, value):
        return self._set_prop('command_list', value)

    @property
    def osd_align_y(self):
        return self._get_prop('osd_align_y')

    @osd_align_y.setter
    def osd_align_y(self, value):
        return self._set_prop('osd_align_y', value)

    @property
    def demuxer_mkv_subtitle_preroll_secs_index(self):
        return self._get_prop('demuxer_mkv_subtitle_preroll_secs_index')

    @demuxer_mkv_subtitle_preroll_secs_index.setter
    def demuxer_mkv_subtitle_preroll_secs_index(self, value):
        return self._set_prop('demuxer_mkv_subtitle_preroll_secs_index', value)

    @property
    def packet_video_bitrate(self):
        return self._get_prop('packet_video_bitrate')

    @packet_video_bitrate.setter
    def packet_video_bitrate(self, value):
        return self._set_prop('packet_video_bitrate', value)

    @property
    def audio_device(self):
        return self._get_prop('audio_device')

    @audio_device.setter
    def audio_device(self, value):
        return self._set_prop('audio_device', value)

    @property
    def cache_dir(self):
        return self._get_prop('cache_dir')

    @cache_dir.setter
    def cache_dir(self, value):
        return self._set_prop('cache_dir', value)

    @property
    def audio_codec_name(self):
        return self._get_prop('audio_codec_name')

    @audio_codec_name.setter
    def audio_codec_name(self, value):
        return self._set_prop('audio_codec_name', value)

    @property
    def dvbin_file(self):
        return self._get_prop('dvbin_file')

    @dvbin_file.setter
    def dvbin_file(self, value):
        return self._set_prop('dvbin_file', value)

    @property
    def dscale_blur(self):
        return self._get_prop('dscale_blur')

    @dscale_blur.setter
    def dscale_blur(self, value):
        return self._set_prop('dscale_blur', value)

    @property
    def jack_autostart(self):
        return self._get_prop('jack_autostart')

    @jack_autostart.setter
    def jack_autostart(self, value):
        return self._set_prop('jack_autostart', value)

    @property
    def rebase_start_time(self):
        return self._get_prop('rebase_start_time')

    @rebase_start_time.setter
    def rebase_start_time(self, value):
        return self._set_prop('rebase_start_time', value)

    @property
    def sub_filter_regex_enable(self):
        return self._get_prop('sub_filter_regex_enable')

    @sub_filter_regex_enable.setter
    def sub_filter_regex_enable(self, value):
        return self._set_prop('sub_filter_regex_enable', value)

    @property
    def autofit(self):
        return self._get_prop('autofit')

    @autofit.setter
    def autofit(self, value):
        return self._set_prop('autofit', value)

    @property
    def log_file(self):
        return self._get_prop('log_file')

    @log_file.setter
    def log_file(self, value):
        return self._set_prop('log_file', value)

    @property
    def mkv_subtitle_preroll(self):
        return self._get_prop('mkv_subtitle_preroll')

    @mkv_subtitle_preroll.setter
    def mkv_subtitle_preroll(self, value):
        return self._set_prop('mkv_subtitle_preroll', value)

    @property
    def cover_art_files(self):
        return self._get_prop('cover_art_files')

    @cover_art_files.setter
    def cover_art_files(self, value):
        return self._set_prop('cover_art_files', value)

    @property
    def video_sync_max_audio_change(self):
        return self._get_prop('video_sync_max_audio_change')

    @video_sync_max_audio_change.setter
    def video_sync_max_audio_change(self, value):
        return self._set_prop('video_sync_max_audio_change', value)

    @property
    def of(self):
        return self._get_prop('of')

    @of.setter
    def of(self, value):
        return self._set_prop('of', value)

    @property
    def avsync(self):
        return self._get_prop('avsync')

    @avsync.setter
    def avsync(self, value):
        return self._set_prop('avsync', value)

    @property
    def vo_image_high_bit_depth(self):
        return self._get_prop('vo_image_high_bit_depth')

    @vo_image_high_bit_depth.setter
    def vo_image_high_bit_depth(self, value):
        return self._set_prop('vo_image_high_bit_depth', value)

    @property
    def perf_info(self):
        return self._get_prop('perf_info')

    @perf_info.setter
    def perf_info(self, value):
        return self._set_prop('perf_info', value)

    @property
    def sub_pos(self):
        return self._get_prop('sub_pos')

    @sub_pos.setter
    def sub_pos(self, value):
        return self._set_prop('sub_pos', value)

    @property
    def dscale_window(self):
        return self._get_prop('dscale_window')

    @dscale_window.setter
    def dscale_window(self, value):
        return self._set_prop('dscale_window', value)

    @property
    def vo_passes(self):
        return self._get_prop('vo_passes')

    @vo_passes.setter
    def vo_passes(self, value):
        return self._set_prop('vo_passes', value)

    @property
    def media_title(self):
        return self._get_prop('media_title')

    @media_title.setter
    def media_title(self, value):
        return self._set_prop('media_title', value)

    @property
    def hr_seek_demuxer_offset(self):
        return self._get_prop('hr_seek_demuxer_offset')

    @hr_seek_demuxer_offset.setter
    def hr_seek_demuxer_offset(self, value):
        return self._set_prop('hr_seek_demuxer_offset', value)

    @property
    def chapter_metadata(self):
        return self._get_prop('chapter_metadata')

    @chapter_metadata.setter
    def chapter_metadata(self, value):
        return self._set_prop('chapter_metadata', value)

    @property
    def dscale_wblur(self):
        return self._get_prop('dscale_wblur')

    @dscale_wblur.setter
    def dscale_wblur(self, value):
        return self._set_prop('dscale_wblur', value)

    @property
    def loop_file(self):
        return self._get_prop('loop_file')

    @loop_file.setter
    def loop_file(self, value):
        return self._set_prop('loop_file', value)

    @property
    def vo(self):
        return self._get_prop('vo')

    @vo.setter
    def vo(self, value):
        return self._set_prop('vo', value)

    @property
    def estimated_vf_fps(self):
        return self._get_prop('estimated_vf_fps')

    @estimated_vf_fps.setter
    def estimated_vf_fps(self, value):
        return self._set_prop('estimated_vf_fps', value)

    @property
    def input_vo_keyboard(self):
        return self._get_prop('input_vo_keyboard')

    @input_vo_keyboard.setter
    def input_vo_keyboard(self, value):
        return self._set_prop('input_vo_keyboard', value)

    @property
    def demuxer_lavf_list(self):
        return self._get_prop('demuxer_lavf_list')

    @demuxer_lavf_list.setter
    def demuxer_lavf_list(self, value):
        return self._set_prop('demuxer_lavf_list', value)

    @property
    def demuxer_cache_state(self):
        return self._get_prop('demuxer_cache_state')

    @demuxer_cache_state.setter
    def demuxer_cache_state(self, value):
        return self._set_prop('demuxer_cache_state', value)

    @property
    def demuxer_lavf_hacks(self):
        return self._get_prop('demuxer_lavf_hacks')

    @demuxer_lavf_hacks.setter
    def demuxer_lavf_hacks(self, value):
        return self._set_prop('demuxer_lavf_hacks', value)

    @property
    def opengl_check_pattern_b(self):
        return self._get_prop('opengl_check_pattern_b')

    @opengl_check_pattern_b.setter
    def opengl_check_pattern_b(self, value):
        return self._set_prop('opengl_check_pattern_b', value)

    @property
    def network_timeout(self):
        return self._get_prop('network_timeout')

    @network_timeout.setter
    def network_timeout(self, value):
        return self._set_prop('network_timeout', value)

    @property
    def resume_playback(self):
        return self._get_prop('resume_playback')

    @resume_playback.setter
    def resume_playback(self, value):
        return self._set_prop('resume_playback', value)

    @property
    def sub_text_font(self):
        return self._get_prop('sub_text_font')

    @sub_text_font.setter
    def sub_text_font(self, value):
        return self._set_prop('sub_text_font', value)

    @property
    def vo_vaapi_scaling(self):
        return self._get_prop('vo_vaapi_scaling')

    @vo_vaapi_scaling.setter
    def vo_vaapi_scaling(self, value):
        return self._set_prop('vo_vaapi_scaling', value)

    @property
    def zimg_scaler_chroma_param_a(self):
        return self._get_prop('zimg_scaler_chroma_param_a')

    @zimg_scaler_chroma_param_a.setter
    def zimg_scaler_chroma_param_a(self, value):
        return self._set_prop('zimg_scaler_chroma_param_a', value)

    @property
    def vo_image_jpeg_quality(self):
        return self._get_prop('vo_image_jpeg_quality')

    @vo_image_jpeg_quality.setter
    def vo_image_jpeg_quality(self, value):
        return self._set_prop('vo_image_jpeg_quality', value)

    @property
    def screenshot_format(self):
        return self._get_prop('screenshot_format')

    @screenshot_format.setter
    def screenshot_format(self, value):
        return self._set_prop('screenshot_format', value)

    @property
    def tscale_antiring(self):
        return self._get_prop('tscale_antiring')

    @tscale_antiring.setter
    def tscale_antiring(self, value):
        return self._set_prop('tscale_antiring', value)

    @property
    def oacopts(self):
        return self._get_prop('oacopts')

    @oacopts.setter
    def oacopts(self, value):
        return self._set_prop('oacopts', value)

    @property
    def loop(self):
        return self._get_prop('loop')

    @loop.setter
    def loop(self, value):
        return self._set_prop('loop', value)

    @property
    def vd(self):
        return self._get_prop('vd')

    @vd.setter
    def vd(self, value):
        return self._set_prop('vd', value)

    @property
    def sub_text(self):
        return self._get_prop('sub_text')

    @sub_text.setter
    def sub_text(self, value):
        return self._set_prop('sub_text', value)

    @property
    def drm_video_plane_id(self):
        return self._get_prop('drm_video_plane_id')

    @drm_video_plane_id.setter
    def drm_video_plane_id(self, value):
        return self._set_prop('drm_video_plane_id', value)

    @property
    def scale_window(self):
        return self._get_prop('scale_window')

    @scale_window.setter
    def scale_window(self, value):
        return self._set_prop('scale_window', value)

    @property
    def osd_height(self):
        return self._get_prop('osd_height')

    @osd_height.setter
    def osd_height(self, value):
        return self._set_prop('osd_height', value)

    @property
    def video_osd(self):
        return self._get_prop('video_osd')

    @video_osd.setter
    def video_osd(self, value):
        return self._set_prop('video_osd', value)

    @property
    def format(self):
        return self._get_prop('format')

    @format.setter
    def format(self, value):
        return self._set_prop('format', value)

    @property
    def spugauss(self):
        return self._get_prop('spugauss')

    @spugauss.setter
    def spugauss(self, value):
        return self._set_prop('spugauss', value)

    @property
    def osd_font_provider(self):
        return self._get_prop('osd_font_provider')

    @osd_font_provider.setter
    def osd_font_provider(self, value):
        return self._set_prop('osd_font_provider', value)

    @property
    def audio(self):
        return self._get_prop('audio')

    @audio.setter
    def audio(self, value):
        return self._set_prop('audio', value)

    @property
    def image_subs_video_resolution(self):
        return self._get_prop('image_subs_video_resolution')

    @image_subs_video_resolution.setter
    def image_subs_video_resolution(self, value):
        return self._set_prop('image_subs_video_resolution', value)

    @property
    def sub_text_font_size(self):
        return self._get_prop('sub_text_font_size')

    @sub_text_font_size.setter
    def sub_text_font_size(self, value):
        return self._set_prop('sub_text_font_size', value)

    @property
    def screenshot_sw(self):
        return self._get_prop('screenshot_sw')

    @screenshot_sw.setter
    def screenshot_sw(self, value):
        return self._set_prop('screenshot_sw', value)

    @property
    def sub_filter_regex_warn(self):
        return self._get_prop('sub_filter_regex_warn')

    @sub_filter_regex_warn.setter
    def sub_filter_regex_warn(self, value):
        return self._set_prop('sub_filter_regex_warn', value)

    @property
    def playlist_current_pos(self):
        return self._get_prop('playlist_current_pos')

    @playlist_current_pos.setter
    def playlist_current_pos(self, value):
        return self._set_prop('playlist_current_pos', value)

    @property
    def vo_image_png_compression(self):
        return self._get_prop('vo_image_png_compression')

    @vo_image_png_compression.setter
    def vo_image_png_compression(self, value):
        return self._set_prop('vo_image_png_compression', value)

    @property
    def orawts(self):
        return self._get_prop('orawts')

    @orawts.setter
    def orawts(self, value):
        return self._set_prop('orawts', value)

    @property
    def hwdec_preload(self):
        return self._get_prop('hwdec_preload')

    @hwdec_preload.setter
    def hwdec_preload(self, value):
        return self._set_prop('hwdec_preload', value)

    @property
    def tscale_blur(self):
        return self._get_prop('tscale_blur')

    @tscale_blur.setter
    def tscale_blur(self, value):
        return self._set_prop('tscale_blur', value)

    @property
    def msg_module(self):
        return self._get_prop('msg_module')

    @msg_module.setter
    def msg_module(self, value):
        return self._set_prop('msg_module', value)

    @property
    def dscale_param1(self):
        return self._get_prop('dscale_param1')

    @dscale_param1.setter
    def dscale_param1(self, value):
        return self._set_prop('dscale_param1', value)

    @property
    def replaygain_preamp(self):
        return self._get_prop('replaygain_preamp')

    @replaygain_preamp.setter
    def replaygain_preamp(self, value):
        return self._set_prop('replaygain_preamp', value)

    @property
    def opengl_restrict(self):
        return self._get_prop('opengl_restrict')

    @opengl_restrict.setter
    def opengl_restrict(self, value):
        return self._set_prop('opengl_restrict', value)

    @property
    def zimg_scaler_param_b(self):
        return self._get_prop('zimg_scaler_param_b')

    @zimg_scaler_param_b.setter
    def zimg_scaler_param_b(self, value):
        return self._set_prop('zimg_scaler_param_b', value)

    @property
    def scale_taper(self):
        return self._get_prop('scale_taper')

    @scale_taper.setter
    def scale_taper(self, value):
        return self._set_prop('scale_taper', value)

    @property
    def video_output_levels(self):
        return self._get_prop('video_output_levels')

    @video_output_levels.setter
    def video_output_levels(self, value):
        return self._set_prop('video_output_levels', value)

    @property
    def ffmpeg_version(self):
        return self._get_prop('ffmpeg_version')

    @ffmpeg_version.setter
    def ffmpeg_version(self, value):
        return self._set_prop('ffmpeg_version', value)

    @property
    def dvd_speed(self):
        return self._get_prop('dvd_speed')

    @dvd_speed.setter
    def dvd_speed(self, value):
        return self._set_prop('dvd_speed', value)

    @property
    def audio_device_list(self):
        return self._get_prop('audio_device_list')

    @audio_device_list.setter
    def audio_device_list(self, value):
        return self._set_prop('audio_device_list', value)

    @property
    def packet_audio_bitrate(self):
        return self._get_prop('packet_audio_bitrate')

    @packet_audio_bitrate.setter
    def packet_audio_bitrate(self, value):
        return self._set_prop('packet_audio_bitrate', value)

    @property
    def osd_border_size(self):
        return self._get_prop('osd_border_size')

    @osd_border_size.setter
    def osd_border_size(self, value):
        return self._set_prop('osd_border_size', value)

    @property
    def target_peak(self):
        return self._get_prop('target_peak')

    @target_peak.setter
    def target_peak(self, value):
        return self._set_prop('target_peak', value)

    @property
    def drm_atomic(self):
        return self._get_prop('drm_atomic')

    @drm_atomic.setter
    def drm_atomic(self, value):
        return self._set_prop('drm_atomic', value)

    @property
    def hwdec(self):
        return self._get_prop('hwdec')

    @hwdec.setter
    def hwdec(self, value):
        return self._set_prop('hwdec', value)

    @property
    def sub_paths(self):
        return self._get_prop('sub_paths')

    @sub_paths.setter
    def sub_paths(self, value):
        return self._set_prop('sub_paths', value)

    @property
    def vd_lavc_show_all(self):
        return self._get_prop('vd_lavc_show_all')

    @vd_lavc_show_all.setter
    def vd_lavc_show_all(self, value):
        return self._set_prop('vd_lavc_show_all', value)

    @property
    def deband(self):
        return self._get_prop('deband')

    @deband.setter
    def deband(self, value):
        return self._set_prop('deband', value)

    @property
    def playlist_start(self):
        return self._get_prop('playlist_start')

    @playlist_start.setter
    def playlist_start(self, value):
        return self._set_prop('playlist_start', value)

    @property
    def drm_format(self):
        return self._get_prop('drm_format')

    @drm_format.setter
    def drm_format(self, value):
        return self._set_prop('drm_format', value)

    @property
    def metadata_codepage(self):
        return self._get_prop('metadata_codepage')

    @metadata_codepage.setter
    def metadata_codepage(self, value):
        return self._set_prop('metadata_codepage', value)

    @property
    def pause(self):
        return self._get_prop('pause')

    @pause.setter
    def pause(self, value):
        return self._set_prop('pause', value)

    @property
    def dither(self):
        return self._get_prop('dither')

    @dither.setter
    def dither(self, value):
        return self._set_prop('dither', value)

    @property
    def demuxer_max_back_bytes(self):
        return self._get_prop('demuxer_max_back_bytes')

    @demuxer_max_back_bytes.setter
    def demuxer_max_back_bytes(self, value):
        return self._set_prop('demuxer_max_back_bytes', value)

    @property
    def colormatrix_input_range(self):
        return self._get_prop('colormatrix_input_range')

    @colormatrix_input_range.setter
    def colormatrix_input_range(self, value):
        return self._set_prop('colormatrix_input_range', value)

    @property
    def lazy(self):
        return self._get_prop('lazy')

    @lazy.setter
    def lazy(self, value):
        return self._set_prop('lazy', value)

    @property
    def video_scale_y(self):
        return self._get_prop('video_scale_y')

    @video_scale_y.setter
    def video_scale_y(self, value):
        return self._set_prop('video_scale_y', value)

    @property
    def vsync_ratio(self):
        return self._get_prop('vsync_ratio')

    @vsync_ratio.setter
    def vsync_ratio(self, value):
        return self._set_prop('vsync_ratio', value)

    @property
    def seeking(self):
        return self._get_prop('seeking')

    @seeking.setter
    def seeking(self, value):
        return self._set_prop('seeking', value)

    @property
    def display_hidpi_scale(self):
        return self._get_prop('display_hidpi_scale')

    @display_hidpi_scale.setter
    def display_hidpi_scale(self, value):
        return self._set_prop('display_hidpi_scale', value)

    @property
    def vo_tct_width(self):
        return self._get_prop('vo_tct_width')

    @vo_tct_width.setter
    def vo_tct_width(self, value):
        return self._set_prop('vo_tct_width', value)

    @property
    def audio_file_paths(self):
        return self._get_prop('audio_file_paths')

    @audio_file_paths.setter
    def audio_file_paths(self, value):
        return self._set_prop('audio_file_paths', value)

    @property
    def cdrom_device(self):
        return self._get_prop('cdrom_device')

    @cdrom_device.setter
    def cdrom_device(self, value):
        return self._set_prop('cdrom_device', value)

    @property
    def input_conf(self):
        return self._get_prop('input_conf')

    @input_conf.setter
    def input_conf(self, value):
        return self._set_prop('input_conf', value)

    @property
    def opengl_debug(self):
        return self._get_prop('opengl_debug')

    @opengl_debug.setter
    def opengl_debug(self, value):
        return self._set_prop('opengl_debug', value)

    @property
    def ontop(self):
        return self._get_prop('ontop')

    @ontop.setter
    def ontop(self, value):
        return self._set_prop('ontop', value)

    @property
    def sub_font_size(self):
        return self._get_prop('sub_font_size')

    @sub_font_size.setter
    def sub_font_size(self, value):
        return self._set_prop('sub_font_size', value)

    @property
    def cscale_clamp(self):
        return self._get_prop('cscale_clamp')

    @cscale_clamp.setter
    def cscale_clamp(self, value):
        return self._set_prop('cscale_clamp', value)

    @property
    def vo_vdpau_colorkey(self):
        return self._get_prop('vo_vdpau_colorkey')

    @vo_vdpau_colorkey.setter
    def vo_vdpau_colorkey(self, value):
        return self._set_prop('vo_vdpau_colorkey', value)

    @property
    def vd_lavc_dr(self):
        return self._get_prop('vd_lavc_dr')

    @vd_lavc_dr.setter
    def vd_lavc_dr(self, value):
        return self._set_prop('vd_lavc_dr', value)

    @property
    def osdlevel(self):
        return self._get_prop('osdlevel')

    @osdlevel.setter
    def osdlevel(self, value):
        return self._set_prop('osdlevel', value)

    @property
    def gamma(self):
        return self._get_prop('gamma')

    @gamma.setter
    def gamma(self, value):
        return self._set_prop('gamma', value)

    @property
    def stream_dump(self):
        return self._get_prop('stream_dump')

    @stream_dump.setter
    def stream_dump(self, value):
        return self._set_prop('stream_dump', value)

    @property
    def chapter_list(self):
        return self._get_prop('chapter_list')

    @chapter_list.setter
    def chapter_list(self, value):
        return self._set_prop('chapter_list', value)

    @property
    def ass_line_spacing(self):
        return self._get_prop('ass_line_spacing')

    @ass_line_spacing.setter
    def ass_line_spacing(self, value):
        return self._set_prop('ass_line_spacing', value)

    @property
    def tscale_wparam(self):
        return self._get_prop('tscale_wparam')

    @tscale_wparam.setter
    def tscale_wparam(self, value):
        return self._set_prop('tscale_wparam', value)

    @property
    def cookies_file(self):
        return self._get_prop('cookies_file')

    @cookies_file.setter
    def cookies_file(self, value):
        return self._set_prop('cookies_file', value)

    @property
    def config(self):
        return self._get_prop('config')

    @config.setter
    def config(self, value):
        return self._set_prop('config', value)

    @property
    def sigmoid_slope(self):
        return self._get_prop('sigmoid_slope')

    @sigmoid_slope.setter
    def sigmoid_slope(self, value):
        return self._set_prop('sigmoid_slope', value)

    @property
    def sub_auto(self):
        return self._get_prop('sub_auto')

    @sub_auto.setter
    def sub_auto(self, value):
        return self._set_prop('sub_auto', value)

    @property
    def drm_osd_plane_id(self):
        return self._get_prop('drm_osd_plane_id')

    @drm_osd_plane_id.setter
    def drm_osd_plane_id(self, value):
        return self._set_prop('drm_osd_plane_id', value)

    @property
    def autosub(self):
        return self._get_prop('autosub')

    @autosub.setter
    def autosub(self, value):
        return self._set_prop('autosub', value)

    @property
    def cache_buffering_state(self):
        return self._get_prop('cache_buffering_state')

    @cache_buffering_state.setter
    def cache_buffering_state(self, value):
        return self._set_prop('cache_buffering_state', value)

    @property
    def sub_margin_y(self):
        return self._get_prop('sub_margin_y')

    @sub_margin_y.setter
    def sub_margin_y(self, value):
        return self._set_prop('sub_margin_y', value)

    @property
    def playlist_pos(self):
        return self._get_prop('playlist_pos')

    @playlist_pos.setter
    def playlist_pos(self, value):
        return self._set_prop('playlist_pos', value)

    @property
    def osd_duration(self):
        return self._get_prop('osd_duration')

    @osd_duration.setter
    def osd_duration(self, value):
        return self._set_prop('osd_duration', value)

    @property
    def opengl_shader_cache_dir(self):
        return self._get_prop('opengl_shader_cache_dir')

    @opengl_shader_cache_dir.setter
    def opengl_shader_cache_dir(self, value):
        return self._set_prop('opengl_shader_cache_dir', value)

    @property
    def demuxer_seekable_cache(self):
        return self._get_prop('demuxer_seekable_cache')

    @demuxer_seekable_cache.setter
    def demuxer_seekable_cache(self, value):
        return self._set_prop('demuxer_seekable_cache', value)

    @property
    def swapchain_depth(self):
        return self._get_prop('swapchain_depth')

    @swapchain_depth.setter
    def swapchain_depth(self, value):
        return self._set_prop('swapchain_depth', value)

    @property
    def opengl_hwdec_interop(self):
        return self._get_prop('opengl_hwdec_interop')

    @opengl_hwdec_interop.setter
    def opengl_hwdec_interop(self, value):
        return self._set_prop('opengl_hwdec_interop', value)

    @property
    def vd_lavc_skipframe(self):
        return self._get_prop('vd_lavc_skipframe')

    @vd_lavc_skipframe.setter
    def vd_lavc_skipframe(self, value):
        return self._set_prop('vd_lavc_skipframe', value)

    @property
    def sub_ass_hinting(self):
        return self._get_prop('sub_ass_hinting')

    @sub_ass_hinting.setter
    def sub_ass_hinting(self, value):
        return self._set_prop('sub_ass_hinting', value)

    @property
    def demuxer_rawaudio_rate(self):
        return self._get_prop('demuxer_rawaudio_rate')

    @demuxer_rawaudio_rate.setter
    def demuxer_rawaudio_rate(self, value):
        return self._set_prop('demuxer_rawaudio_rate', value)

    @property
    def file_size(self):
        return self._get_prop('file_size')

    @file_size.setter
    def file_size(self, value):
        return self._set_prop('file_size', value)

    @property
    def raw(self):
        return self._get_prop('raw')

    @raw.setter
    def raw(self, value):
        return self._set_prop('raw', value)

    @property
    def alsa_mixer_device(self):
        return self._get_prop('alsa_mixer_device')

    @alsa_mixer_device.setter
    def alsa_mixer_device(self, value):
        return self._set_prop('alsa_mixer_device', value)

    @property
    def input_doubleclick_time(self):
        return self._get_prop('input_doubleclick_time')

    @input_doubleclick_time.setter
    def input_doubleclick_time(self, value):
        return self._set_prop('input_doubleclick_time', value)

    @property
    def aspect(self):
        return self._get_prop('aspect')

    @aspect.setter
    def aspect(self, value):
        return self._set_prop('aspect', value)

    @property
    def vulkan_swap_mode(self):
        return self._get_prop('vulkan_swap_mode')

    @vulkan_swap_mode.setter
    def vulkan_swap_mode(self, value):
        return self._set_prop('vulkan_swap_mode', value)

    @property
    def fs(self):
        return self._get_prop('fs')

    @fs.setter
    def fs(self, value):
        return self._set_prop('fs', value)

    @property
    def dvbin_channel_switch_offset(self):
        return self._get_prop('dvbin_channel_switch_offset')

    @dvbin_channel_switch_offset.setter
    def dvbin_channel_switch_offset(self, value):
        return self._set_prop('dvbin_channel_switch_offset', value)

    @property
    def vo_vdpau_hqscaling(self):
        return self._get_prop('vo_vdpau_hqscaling')

    @vo_vdpau_hqscaling.setter
    def vo_vdpau_hqscaling(self, value):
        return self._set_prop('vo_vdpau_hqscaling', value)

    @property
    def dvbin_prog(self):
        return self._get_prop('dvbin_prog')

    @dvbin_prog.setter
    def dvbin_prog(self, value):
        return self._set_prop('dvbin_prog', value)

    @property
    def demuxer_rawaudio_format(self):
        return self._get_prop('demuxer_rawaudio_format')

    @demuxer_rawaudio_format.setter
    def demuxer_rawaudio_format(self, value):
        return self._set_prop('demuxer_rawaudio_format', value)

    @property
    def pulse_host(self):
        return self._get_prop('pulse_host')

    @pulse_host.setter
    def pulse_host(self, value):
        return self._set_prop('pulse_host', value)

    @property
    def mouse_movements(self):
        return self._get_prop('mouse_movements')

    @mouse_movements.setter
    def mouse_movements(self, value):
        return self._set_prop('mouse_movements', value)

class MPVMethod(MPVBase):

    def wait_until_paused(self, *args, **kwargs):
        return self._run_method('wait_until_paused', self, *args, **kwargs)

    def audio_reload(self, audio_id, *args, **kwargs):
        return self._run_method('audio_reload', self, audio_id, *args, **kwargs)

    def playlist_next(self, mode, *args, **kwargs):
        return self._run_method('playlist_next', self, mode, *args, **kwargs)

    def property_observer(self, name, *args, **kwargs):
        return self._run_method('property_observer', self, name, *args, **kwargs)

    def video_remove(self, video_id, *args, **kwargs):
        return self._run_method('video_remove', self, video_id, *args, **kwargs)

    def script_message_to(self, target, *args, **kwargs):
        return self._run_method('script_message_to', self, target, *args, **kwargs)

    def property_multiply(self, name, factor, *args, **kwargs):
        return self._run_method('property_multiply', self, name, factor, *args, **kwargs)

    def playlist_remove(self, index, *args, **kwargs):
        return self._run_method('playlist_remove', self, index, *args, **kwargs)

    def playlist_clear(self, *args, **kwargs):
        return self._run_method('playlist_clear', self, *args, **kwargs)

    def playlist_move(self, index1, index2, *args, **kwargs):
        return self._run_method('playlist_move', self, index1, index2, *args, **kwargs)

    def wait_for_event(self, *event_types, **kwargs):
        return self._run_method('wait_for_event', self, *event_types, **kwargs)

    def unobserve_all_properties(self, handler, *args, **kwargs):
        return self._run_method('unobserve_all_properties', self, handler, *args, **kwargs)

    def register_event_callback(self, callback, *args, **kwargs):
        return self._run_method('register_event_callback', self, callback, *args, **kwargs)

    def sub_reload(self, sub_id, *args, **kwargs):
        return self._run_method('sub_reload', self, sub_id, *args, **kwargs)

    def wait_for_shutdown(self, *args, **kwargs):
        return self._run_method('wait_for_shutdown', self, *args, **kwargs)

    def property_add(self, name, value, *args, **kwargs):
        return self._run_method('property_add', self, name, value, *args, **kwargs)

    def wait_until_playing(self, *args, **kwargs):
        return self._run_method('wait_until_playing', self, *args, **kwargs)

    def script_message(self, *args, **kwargs):
        return self._run_method('script_message', self, *args, **kwargs)

    def free_overlay_id(self, overlay_id, *args, **kwargs):
        return self._run_method('free_overlay_id', self, overlay_id, *args, **kwargs)

    def wait_for_playback(self, *args, **kwargs):
        return self._run_method('wait_for_playback', self, *args, **kwargs)

    def overlay_remove(self, overlay_id, *args, **kwargs):
        return self._run_method('overlay_remove', self, overlay_id, *args, **kwargs)

    def screenshot_raw(self, includes, *args, **kwargs):
        return self._run_method('screenshot_raw', self, includes, *args, **kwargs)

    def remove_overlay(self, overlay_id, *args, **kwargs):
        return self._run_method('remove_overlay', self, overlay_id, *args, **kwargs)

    def loadlist(self, playlist, mode, *args, **kwargs):
        return self._run_method('loadlist', self, playlist, mode, *args, **kwargs)

    def set_loglevel(self, level, *args, **kwargs):
        return self._run_method('set_loglevel', self, level, *args, **kwargs)

    def node_command(self, name, *args, **kwargs):
        return self._run_method('node_command', self, name, *args, **kwargs)

    def toggle_osd(self, *args, **kwargs):
        return self._run_method('toggle_osd', self, *args, **kwargs)

    def rescan_external_files(self, mode, *args, **kwargs):
        return self._run_method('rescan_external_files', self, mode, *args, **kwargs)

    def message_handler(self, target, *args, **kwargs):
        return self._run_method('message_handler', self, target, *args, **kwargs)

    def unregister_key_binding(self, keydef, *args, **kwargs):
        return self._run_method('unregister_key_binding', self, keydef, *args, **kwargs)

    def sub_remove(self, sub_id, *args, **kwargs):
        return self._run_method('sub_remove', self, sub_id, *args, **kwargs)

    def print_text(self, text, *args, **kwargs):
        return self._run_method('print_text', self, text, *args, **kwargs)

    def unobserve_property(self, name, handler, *args, **kwargs):
        return self._run_method('unobserve_property', self, name, handler, *args, **kwargs)

    def quit_watch_later(self, code, *args, **kwargs):
        return self._run_method('quit_watch_later', self, code, *args, **kwargs)

    def keyup(self, name, *args, **kwargs):
        return self._run_method('keyup', self, name, *args, **kwargs)

    def playlist_shuffle(self, *args, **kwargs):
        return self._run_method('playlist_shuffle', self, *args, **kwargs)

    def cycle(self, name, direction, *args, **kwargs):
        return self._run_method('cycle', self, name, direction, *args, **kwargs)

    def register_stream_protocol(self, proto, open_fn, *args, **kwargs):
        return self._run_method('register_stream_protocol', self, proto, open_fn, *args, **kwargs)

    def run(self, command, *args, **kwargs):
        return self._run_method('run', self, command, *args, **kwargs)

    def stop(self, keep_playlist, *args, **kwargs):
        return self._run_method('stop', self, keep_playlist, *args, **kwargs)

    def playlist_play_index(self, idx, *args, **kwargs):
        return self._run_method('playlist_play_index', self, idx, *args, **kwargs)

    def python_stream(self, name, size, *args, **kwargs):
        return self._run_method('python_stream', self, name, size, *args, **kwargs)

    def loadfile(self, filename, mode, *args, **options):
        return self._run_method('loadfile', self, filename, mode, *args, **options)

    def option_info(self, name, *args, **kwargs):
        return self._run_method('option_info', self, name, *args, **kwargs)

    def video_reload(self, video_id, *args, **kwargs):
        return self._run_method('video_reload', self, video_id, *args, **kwargs)

    def play(self, filename, *args, **kwargs):
        return self._run_method('play', self, filename, *args, **kwargs)

    def sub_seek(self, skip, *args, **kwargs):
        return self._run_method('sub_seek', self, skip, *args, **kwargs)

    def playlist_append(self, filename, *args, **options):
        return self._run_method('playlist_append', self, filename, *args, **options)

    def playlist_unshuffle(self, *args, **kwargs):
        return self._run_method('playlist_unshuffle', self, *args, **kwargs)

    def frame_back_step(self, *args, **kwargs):
        return self._run_method('frame_back_step', self, *args, **kwargs)

    def key_binding(self, keydef, mode, *args, **kwargs):
        return self._run_method('key_binding', self, keydef, mode, *args, **kwargs)

    def register_message_handler(self, target, handler, *args, **kwargs):
        return self._run_method('register_message_handler', self, target, handler, *args, **kwargs)

    def keydown(self, name, *args, **kwargs):
        return self._run_method('keydown', self, name, *args, **kwargs)

    def expand_path(self, path, *args, **kwargs):
        return self._run_method('expand_path', self, path, *args, **kwargs)

    def mouse(self, x, y, button, mode, *args, **kwargs):
        return self._run_method('mouse', self, x, y, button, mode, *args, **kwargs)

    def wait_for_property(self, name, cond, level_sensitive, *args, **kwargs):
        return self._run_method('wait_for_property', self, name, cond, level_sensitive, *args, **kwargs)

    def screenshot(self, includes, mode, *args, **kwargs):
        return self._run_method('screenshot', self, includes, mode, *args, **kwargs)

    def create_file_overlay(self, filename, size, stride, pos, *args, **kwargs):
        return self._run_method('create_file_overlay', self, filename, size, stride, pos, *args, **kwargs)

    def frame_step(self, *args, **kwargs):
        return self._run_method('frame_step', self, *args, **kwargs)

    def playlist_prev(self, mode, *args, **kwargs):
        return self._run_method('playlist_prev', self, mode, *args, **kwargs)

    def allocate_overlay_id(self, *args, **kwargs):
        return self._run_method('allocate_overlay_id', self, *args, **kwargs)

    def unregister_message_handler(self, target_or_handler, *args, **kwargs):
        return self._run_method('unregister_message_handler', self, target_or_handler, *args, **kwargs)

    def command(self, name, *args, **kwargs):
        return self._run_method('command', self, name, *args, **kwargs)

    def seek(self, amount, reference, precision, *args, **kwargs):
        return self._run_method('seek', self, amount, reference, precision, *args, **kwargs)

    def register_key_binding(self, keydef, callback_or_cmd, mode, *args, **kwargs):
        return self._run_method('register_key_binding', self, keydef, callback_or_cmd, mode, *args, **kwargs)

    def show_text(self, string, duration, level, *args, **kwargs):
        return self._run_method('show_text', self, string, duration, level, *args, **kwargs)

    def create_image_overlay(self, img, pos, *args, **kwargs):
        return self._run_method('create_image_overlay', self, img, pos, *args, **kwargs)

    def event_callback(self, *event_types, **kwargs):
        return self._run_method('event_callback', self, *event_types, **kwargs)

    def discnav(self, command, *args, **kwargs):
        return self._run_method('discnav', self, command, *args, **kwargs)

    def unregister_event_callback(self, callback, *args, **kwargs):
        return self._run_method('unregister_event_callback', self, callback, *args, **kwargs)

    def revert_seek(self, *args, **kwargs):
        return self._run_method('revert_seek', self, *args, **kwargs)

    def keypress(self, name, *args, **kwargs):
        return self._run_method('keypress', self, name, *args, **kwargs)

    def write_watch_later_config(self, *args, **kwargs):
        return self._run_method('write_watch_later_config', self, *args, **kwargs)

    def check_core_alive(self, *args, **kwargs):
        return self._run_method('check_core_alive', self, *args, **kwargs)

    def video_add(self, url, flags, title, lang, *args, **kwargs):
        return self._run_method('video_add', self, url, flags, title, lang, *args, **kwargs)

    def overlay_add(self, overlay_id, x, y, file_or_fd, offset, fmt, w, h, stride, *args, **kwargs):
        return self._run_method('overlay_add', self, overlay_id, x, y, file_or_fd, offset, fmt, w, h, stride, *args, **kwargs)

    def audio_add(self, url, flags, title, lang, *args, **kwargs):
        return self._run_method('audio_add', self, url, flags, title, lang, *args, **kwargs)

    def keybind(self, name, command, *args, **kwargs):
        return self._run_method('keybind', self, name, command, *args, **kwargs)

    def audio_remove(self, audio_id, *args, **kwargs):
        return self._run_method('audio_remove', self, audio_id, *args, **kwargs)

    def sub_step(self, skip, *args, **kwargs):
        return self._run_method('sub_step', self, skip, *args, **kwargs)

    def prepare_and_wait_for_event(self, *args, **kwds):
        return self._run_method('prepare_and_wait_for_event', self, *args, **kwds)

    def sub_add(self, url, flags, title, lang, *args, **kwargs):
        return self._run_method('sub_add', self, url, flags, title, lang, *args, **kwargs)

    def expand_text(self, text, *args, **kwargs):
        return self._run_method('expand_text', self, text, *args, **kwargs)

    def screenshot_to_file(self, filename, includes, *args, **kwargs):
        return self._run_method('screenshot_to_file', self, filename, includes, *args, **kwargs)

    def show_progress(self, *args, **kwargs):
        return self._run_method('show_progress', self, *args, **kwargs)

    def on_key_press(self, keydef, mode, *args, **kwargs):
        return self._run_method('on_key_press', self, keydef, mode, *args, **kwargs)

    def python_stream_catchall(self, cb, *args, **kwargs):
        return self._run_method('python_stream_catchall', self, cb, *args, **kwargs)

    def observe_property(self, name, handler, *args, **kwargs):
        return self._run_method('observe_property', self, name, handler, *args, **kwargs)

    def prepare_and_wait_for_property(self, *args, **kwds):
        return self._run_method('prepare_and_wait_for_property', self, *args, **kwds)

class MPV(MPVProperty, MPVMethod):
    pass
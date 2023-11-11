import sublime
from os import path
import os


root_dir = path.split(__file__)[0]
base_name = path.split(root_dir)[1]

settings_file = 'FastOlympicCoding.sublime-settings'

default_settings_file = 'FastOlympicCoding ({os}).sublime-settings'.format(
	os={ 'windows': 'Windows', 'linux': 'Linux', 'osx': 'OSX' }[sublime.platform().lower()]
)

tests_file_suffix = ':tests'
tests_relative_dir = ''

settings = {}
run_supported_exts = set()

def get_settings():
	return settings

def init_settings(_settings):
	global settings
	settings = _settings

def is_run_supported_ext(ext):
	_run_settings = get_settings().get('run_settings', None)
	if _run_settings is not None:
		for option in _run_settings:
			if ext in option['extensions']:
				return True
	return False

def get_supported_exts(lang):
	_run_settings = get_settings().get('run_settings', None)
	if _run_settings is not None:
		for option in _run_settings:
			if option['name'] == lang:
				return option['extensions']
		return []
	return []

def is_lang_view(view, lang):
	if view.file_name() is None: return False
	return path.splitext(view.file_name())[1][1:] in get_supported_exts(lang)

def try_load_settings():
	_settings = sublime.load_settings(settings_file)
	if _settings is None:
		sublime.set_timeout_async(load_settings, 200)
	else:
		init_settings(_settings)
		sublime.status_message('FastOlympicCoding: settings loaded')

def plugin_loaded():
	sublime.set_timeout(try_load_settings, 200)

def get_tests_file_suffix():
	return get_settings().get('tests_file_suffix') or tests_file_suffix

def get_tests_file_path(file):
	dirname = os.path.join(os.path.dirname(file),
		get_settings().get('tests_relative_dir') or tests_relative_dir)

	if not os.path.exists(dirname):
		os.makedirs(dirname)

	filename = os.path.basename(file) + get_tests_file_suffix()
	
	return os.path.join(dirname, filename)
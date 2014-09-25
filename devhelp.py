import sublime
import sublime_plugin
import os
import subprocess
import shutil


def get_settings():
    devhelp_path = sublime.packages_path() + '/Devhelp'
    user_path = sublime.packages_path() + '/User'

    if not os.path.isdir(user_path):
        os.mkdir(user_path)

    default_settings_path = devhelp_path + '/Devhelp.sublime-settings'
    user_settings_path = user_path + '/Devhelp.sublime-settings'
    if not os.path.exists(user_settings_path):
        if sublime.version() >= '3000':
            zs = sublime.load_resource("Packages/Devhelp/Devhelp.sublime-settings")
            with open(user_settings_path, "w") as f:
                f.write(zs)
        else:
            shutil.copyfile(default_settings_path, user_settings_path)

    return sublime.load_settings('Devhelp.sublime-settings')


def open_devhelp(text):
    devhelp_exe = get_settings().get('devhelp_command')

    if os.path.isfile(devhelp_exe):
        try:
            cmd = []
            cmd.append(devhelp_exe)
            cmd.append(u"-s")
            cmd.append(text)
            subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
        except Exception as e:
            sublime.status_message("Devhelp - (%s)" % (e))
    else:
        sublime.error_message('Could not find your %s executable.\n\nPlease edit Devhelp.sublime-settings' % (devhelp_exe))


class DevhelpSearchSelectionCommand(sublime_plugin.TextCommand):
    """
    Search the selected text or the current word
    """
    def run(self, edit):

        querys = []
        for region in self.view.sel():
            if region.empty():
                # if we have no selection grab the current word
                word = self.view.word(region)
                if not word.empty():
                    querys.append(self.view.substr(word))
            else:
                # append the selection
                if not region.empty():
                    querys.append(self.view.substr(region))


        if len(querys) != 0:
            selection = " ".join(querys)
            print(selection)
            open_devhelp(selection)
        else:
            sublime.status_message(" Nothing to search !")
            print("Devhelp: Nothing to search !")


class DevhelpSearchCommand(sublime_plugin.TextCommand):

    last_text = ''

    def run(self, edit):
        view = self.view
        self.view_panel = view.window().show_input_panel('Search in Devhelp for:', self.last_text, self.after_input, self.on_change, None)
        self.view_panel.set_name('devhelp_command_bar')

    def after_input(self, text):
        if text.strip() == "":
            self.last_text = ''
            sublime.status_message("No text was entered")
            return
        else:
            open_devhelp(text)

    def on_change(self, text):
        if text.strip() == "":
            return

        self.last_text = text.strip()

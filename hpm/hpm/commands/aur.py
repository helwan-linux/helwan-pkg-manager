# hpm/commands/aur.py

import os
import subprocess
from rich.console import Console
from hpm.utils import log
from hpm.i18n import get_translation
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

console = Console()

def find_aur_helper():
    """
    Finds an installed AUR helper (yay or paru) on the system.
    Returns the path to the helper if found, otherwise returns None.
    """
    aur_helpers = ["yay", "paru"]
    for helper in aur_helpers:
        helper_path = os.path.join(PACMAN_PATH, helper)
        if os.path.exists(helper_path):
            return helper_path
    return None

def aur_main(args: list[str], dry_run: bool, force: bool = False, lang: str = 'en'):
    """
    Manages packages from the Arch User Repository (AUR).
    """
    _ = get_translation(lang)
    commands_dict = _('commands')

    log.info(_('command_aur_searching_helper'))
    aur_helper = find_aur_helper()

    if not aur_helper:
        log.error(_('command_aur_error_no_helper_found'))
        log.info(_('command_aur_helper_install_info'))
        return

    log.info(_('command_aur_using_helper').format(helper=os.path.basename(aur_helper)))

    if not args:
        log.error(_('command_aur_error_no_action_provided'))
        return

    action = args[0].lower()
    packages = args[1:]
    
    cmd = [aur_helper]
    
    # Get the lists of keywords from the nested 'commands' dictionary, including the English keywords
    install_keywords = commands_dict['install']['aliases']
    remove_keywords = commands_dict['remove']['aliases']
    search_keywords = commands_dict['search']['aliases']
    upgrade_keywords = commands_dict['upgrade']['aliases']
    
    if action in install_keywords:
        if not packages:
            log.error(_('command_aur_error_no_package_provided'))
            return
        cmd.extend(['-S', '--needed'])
        cmd.extend(packages)
        log.info(_('command_aur_installing_packages').format(packages=', '.join(packages)))

    elif action in remove_keywords:
        if not packages:
            log.error(_('command_aur_error_no_package_provided_remove'))
            return
        cmd.extend(['-Rns'])
        cmd.extend(packages)
        log.info(_('command_aur_removing_packages').format(packages=', '.join(packages)))

    elif action in search_keywords:
        if not packages:
            log.error(_('command_aur_error_no_search_term_provided'))
            return
        cmd.extend(['-Ss'])
        cmd.extend(packages)
        log.info(_('command_aur_searching_for_packages').format(packages=', '.join(packages)))

    elif action in upgrade_keywords:
        cmd.extend(['-Syu'])
        log.info(_('command_aur_upgrading_packages'))
        
    else:
        log.error(_('command_aur_error_unknown_action').format(action=action))
        return
        
    if force:
        cmd.append('--noconfirm')
    
    if dry_run:
        log.warning(_('dry_run_warning'))
        log.info(_('dry_run_command_info').format(command=' '.join(cmd)))
        return

    log.debug(f"Running command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd)
        log.success(_('operation_completed').format(action=action))
    except FileNotFoundError:
        log.error(_('command_aur_error_helper_not_found'))
    except Exception as e:
        log.error(_('command_aur_error_unexpected_error').format(error=e))

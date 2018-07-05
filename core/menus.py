#!/usr/bin/env python

main_menu = {
    #command : function
    'modules':'show_modules',
    'new_module':'generate_module_class',
    'update':'update_tool',
    'clear':'clear_screen',
    'help':'show_help',
    'exit':'exit_blackowl',
    'use':'show_help'
}

cmd_help = {
    #command : description
    'modules':'Show module listing',
    'new_module':'Generate a new module',
    'use':'Load module (use <module name>)',
    'clear':'Clear current screen',
    'update':'Update tool',
    'help':'Show this list of commands',
    'exit':'Close Blackowl'
}


module_menu = {
    #command : description
    'show_options':'Show module options',
    'set':'Set value from element (set <option>=<value>)',
    'run':'Run current module',
    'export':'Export module return data',
    'exit':'Exit current module',
    'clear':'Clear screen',
    'help':'Show this list of commands'
}



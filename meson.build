project('gin',
  version: '0.1',
  license: 'LGPL3'
)

application_id = 'com.belmoussaoui.Gin'

find_program('update-mime-database', required: true)
find_program('gtk-update-icon-cache', required: true)


subdir('data')


meson.add_install_script('meson_post_install.py')

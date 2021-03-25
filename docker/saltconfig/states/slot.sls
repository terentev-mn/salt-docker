file-in-user-home:
  file.copy:
    - name: __slot__:salt:user.info(root).home ~ /subdirectory
    - source: salt://somefile
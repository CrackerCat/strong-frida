# strong-frida

make frida strong, bypass frida detection.

automatically compile frida using github actions

## Anti Frida tricks

[Anti Frida tricks](docs/README.md)

## Features

old sh scripts deprecated.
[here](patch/deprecated)

new patch files from @hluwa. [here](patch/frida-core)

```
$ tree patch/frida-core/
patch/frida-core/
├── 0001-string_frida_rpc.patch
├── 0002-io_re_frida_server.patch
├── 0003-pipe_linjector.patch
├── 0004-io_frida_agent_so.patch
├── 0005-symbol_frida_agent_main.patch
├── 0006-thread_gum_js_loop.patch
├── 0007-thread_gmain.patch
└── 0008-protocol_unexpected_command.patch
```

## References

https://github.com/hluwa/strongR-frida-android

https://github.com/qtfreet00/AntiFrida

https://github.com/darvincisec/DetectFrida

https://github.com/b-mueller/frida-detection-demo

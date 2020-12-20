sed -i 's/re.frida.server/re.feicong.server/g' frida-core/server/server.vala
sed -i 's/frida-agent/feicong-agent/g' frida-core/src/embed-agent.sh
sed -i 's/get_frida_agent/get_feicong_agent/g' frida-core/src/linux/linux-host-session.vala
sed -i 's/frida-agent/feicong-agent/g' frida-core/src/linux/linux-host-session.vala
FROM debian:12

RUN apt-get update && apt-get install -y \
    build-essential git cmake wget unzip ca-certificates \
    libsdl2-2.0-0 libsdl2-dev libopenal-dev libgl1-mesa-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/quakeserver

# Hämta QuakeSpasm server-build
RUN git clone --depth 1 https://github.com/athre0z/quakespasm.git /opt/quakespasm \
 && cd /opt/quakespasm && ./autogen.sh || true && ./configure && make -j"$(nproc)" \
 && cp quakespasm /usr/local/bin/quakespasm

COPY start.sh /usr/local/bin/start-quake.sh
RUN chmod +x /usr/local/bin/start-quake.sh

EXPOSE 26000/udp
VOLUME ["/game"]

CMD ["/usr/local/bin/start-quake.sh"]
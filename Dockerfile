# JRE base
FROM gcr.io/distroless/java:11

# Environment variables
ENV MC_VERSION="latest" \
    PAPER_BUILD="latest" \
    MC_RAML="4G" \
    MC_RAMH="4G" \
    JAVA_OPTS=""

ADD papermc.sh .
RUN apk update \
    && apk add jq \
    && apk add wget \
    && rm -rf /var/cache/apk/* \
    && mkdir /papermc

# Start script
CMD ["sh", "./papermc.sh"]

# Container setup
EXPOSE 25565/tcp
EXPOSE 25565/udp
VOLUME /papermc

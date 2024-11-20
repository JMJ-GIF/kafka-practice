# ARM64에 호환되는 OpenJDK 이미지 사용
FROM arm64v8/openjdk:11-jdk

# Logstash 설치
ENV LOGSTASH_VERSION=7.10.0
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}-linux-x86_64.tar.gz && \
    tar -xzf logstash-${LOGSTASH_VERSION}-linux-x86_64.tar.gz && \
    mv logstash-${LOGSTASH_VERSION} /usr/share/logstash && \
    rm logstash-${LOGSTASH_VERSION}-linux-x86_64.tar.gz

# Logstash 실행 경로 설정
ENV PATH="/usr/share/logstash/bin:${PATH}"

# 설정 파일 디렉터리 설정
WORKDIR /usr/share/logstash

# Logstash 기본 실행 명령어
CMD ["logstash", "-f", "/usr/share/logstash/pipeline/logstash.conf"]

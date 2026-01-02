import speedtest


def check_internet_speed():
    st = speedtest.Speedtest()

    print('Testing speed')
    download = st.download() / 1_000_000
    upload = st.download() / 1_000_000

    st.get_best_server()
    ping = st.results.ping

    return {
        "download" : round(download, 2),
        "upload" : round(upload, 2),
        "ping" : round(ping, 2),
    }


print(check_internet_speed())

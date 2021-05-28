# -*- coding: utf-8 -*-
import time
import requests


def main():
    test_cnt = 10

    url = input("Input URL: ")
    latency_sum = 0

    for i in range(test_cnt):
        st_t = time.time()
        resp = requests.get(url)
        ed_t = time.time()

        latency = ed_t - st_t
        latency_sum = latency_sum + latency
        print(f"HttpCode: {resp.status_code}, Latency: {latency:.9f} sec")

        time.sleep(0.1)

    print(f"Average: {(latency_sum / test_cnt):.9f} sec")


if "__main__" == __name__:
    main()

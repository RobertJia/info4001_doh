#/usr/bin/bash
#while true; do
        #d=`date "+%d-%m-%y-%H%M%S"`
        #mkdir ./pcaps/
        mkdir ./pcaps/firefox/test_wk7
        #sudo systemctl stop cloudflared
        #sleep 3
        #sudo ln -sf /home/ubuntu/doh_traffic_analysis/code/collection/resolv.conf /etc/resolv.conf

        for i in $(seq 1 5)
        do
                echo $i
                sudo /usr/sbin/tcpdump -i any "port 53 || host 1.1.1.1" -w ./pcaps/firefox/test_wk7/firefox$i.pcap &
                sleep 2
                python3 ./firefox_driver.py $i
                sleep 2
                sudo pkill tcpdump
                sleep 2
                sudo systemd-resolve --flush-caches
                sleep 2
        done
        #sleep 300
        #sudo systemctl start cloudflared
#done

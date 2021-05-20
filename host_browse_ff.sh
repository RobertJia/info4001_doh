#/usr/bin/bash
#while true; do
        d=`date "+%d-%m-%y-%H%M%S"`
        #mkdir ./pcaps/
        mkdir ./pcaps/firefox/host$d
        #sudo systemctl stop cloudflared
        #sleep 3
        #sudo ln -sf /home/ubuntu/doh_traffic_analysis/code/collection/resolv.conf /etc/resolv.conf
#"port 53 || host 1.1.1.1"
        for i in $(seq 0 0)
        do
                echo $i
                sudo /usr/sbin/tcpdump -i any  -w ./pcaps/firefox/host$d/firefox$i.pcap &
                sleep 2
                python3 ./host_ff_driver.py $i
                sleep 2
                sudo pkill tcpdump
                sleep 2
                #sudo systemd-resolve --flush-caches
                
                sleep 2
        done
        sudo killall -HUP mDNSResponder
        #sleep 300
        #sudo systemctl start cloudflared
#done

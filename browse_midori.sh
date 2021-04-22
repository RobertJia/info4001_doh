#/usr/bin/bash
while true; do
        d=`date "+%d-%m-%y-%H%M%S"`
        mkdir ./pcaps/midori/$d
        #sudo systemctl stop cloudflared
        #sleep 3
        sudo ln -sf /home/ubuntu/doh_traffic_analysis/code/collection/resolv.conf /etc/resolv.conf
        for i in $(seq 201 1486)
        do
                echo $i
                sudo /usr/sbin/tcpdump -i any "port 53 || host 1.1.1.1" -w ./pcaps/midori/$d/$i.pcap &
                sleep 2
                python3 ./midori_driver.py $i
		#midori $i --disable-gpu &
		sleep 60
		sudo pkill midori
                sleep 2
                sudo pkill tcpdump
                sleep 2
                sudo systemd-resolve --flush-caches
                sleep 2
        done
        #sleep 300
        #sudo systemctl start cloudflared
done

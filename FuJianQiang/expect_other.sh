#!/bin/bash -x
master_install(){
    expect -c "

    spawn ssh-copy-id -i ~/.ssh/id_rsa.pub uisee@10.0.89.28
    expect {
        "*password*" { send "uisee\r" }
    }
    "

    ssh uisee@10.0.89.28 <<EOF
    ssh-agent -s
    ssh-add
    expect -c "
    spawn ssh-keygen -t rsa
    expect {
        "*" { send ""\r }
    }
    expect {
        "y/n" { send "y"\r }
    }
    expect {
        "passphrase" { send ""\r }
    }
    expect {
        "again" { send ""\r }
    }
    spawn ssh-copy-id -i /home/uisee/.ssh/id_rsa.pub dongweili@10.0.93.39
    expect {
        "password:" { send "uisee"\r }
    }

expect eof
"

EOF
}
    # echo "uisee" | sudo -S apt-get install python3-tk -y

master_install
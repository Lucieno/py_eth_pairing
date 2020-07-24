if [ ! -d ~/rust-installer ]; then 
    mkdir ~/rust-installer
    curl -sL https://static.rust-lang.org/rustup.sh -o ~/rust-installer/rustup.sh
    sh ~/rust-installer/rustup.sh -y
    source $HOME/.cargo/env
    rustup default nightly
    python --version
fi

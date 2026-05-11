#!/bin/bash
#====================================================================
# AI Security Researcher Workspace - Tool Build Script
# Comprehensive tool installation for all security testing modules
#====================================================================

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="${WORKSPACE_ROOT}/setup.log"

# Functions
log() {
    echo -e "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
    log "[INFO] $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
    log "[SUCCESS] $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
    log "[WARNING] $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    log "[ERROR] $1"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then 
        warning "Running as non-root user. Some tools may require sudo."
        return 1
    fi
    return 0
}

check_command() {
    if command -v "$1" &> /dev/null; then
        return 0
    else
        return 1
    fi
}

#====================================================================
# Main Menu
#====================================================================

show_menu() {
    clear
    echo "========================================"
    echo "  AI Security Researcher Workspace"
    echo "  Tool Installation Menu"
    echo "========================================"
    echo ""
    echo "1.  Install Web Security Tools"
    echo "2.  Install Binary/PWN Tools"
    echo "3.  Install Mobile Security Tools"
    echo "4.  Install Domain Penetration Tools"
    echo "5.  Install Anonymity & Proxy Tools"
    echo "6.  Install Blue Team Tools"
    echo "7.  Install Compliance Tools"
    echo "8.  Install Purple Team Tools"
    echo "9.  Install General Security Tools"
    echo "10. Install All Tools"
    echo "11. Show Installed Tools"
    echo "12. Update Tools"
    echo "0.  Exit"
    echo ""
    echo "========================================"
    echo ""
    read -p "Enter your choice [0-12]: " choice
}

#====================================================================
# Web Security Tools Installation
#====================================================================

install_web_tools() {
    info "Installing Web Security Tools..."
    
    # Check if apt is available
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping system packages."
    fi
    
    # Install from apt
    if check_command apt-get; then
        sudo apt-get update -qq
        
        # Core web tools
        sudo apt-get install -y curl wget git python3 python3-pip > /dev/null 2>&1
        
        info "Installing Python web security tools..."
        pip3 install --quiet sqlmap 2>/dev/null || warning "sqlmap installation failed"
        pip3 install --quiet requests beautifulsoup4 2>/dev/null || warning "Basic Python packages failed"
        
        # Directory enumeration
        pip3 install --quiet dirb gobuster 2>/dev/null || info "Installing gobuster from apt..."
        sudo apt-get install -y gobuster > /dev/null 2>&1 || warning "gobuster installation failed"
        
        # Nmap for web scanning
        sudo apt-get install -y nmap > /dev/null 2>&1 || warning "nmap installation failed"
        
        # Burp Suite Community (download required)
        info "Burp Suite requires manual download from PortSwigger"
    fi
    
    # Clone popular tools
    info "Cloning web security tools from GitHub..."
    
    # FFUF - Fast web fuzzer
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/ffuf" ]; then
        git clone --quiet https://github.com/ffuf/ffuf.git "${WORKSPACE_ROOT}/shared/tools/ffuf" 2>/dev/null || warning "FFUF clone failed"
    fi
    
    # Nuclei - vulnerability scanner
    if ! check_command nuclei; then
        sudo -u "$SUDO_USER" bash -c '
        mkdir -p ~/.local/bin
        curl -sL https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei_linux_amd64.zip -o /tmp/nuclei.zip 2>/dev/null || exit 1
        unzip -q /tmp/nuclei.zip -d ~/.local/bin 2>/dev/null || exit 1
        chmod +x ~/.local/bin/nuclei 2>/dev/null || exit 1
        rm /tmp/nuclei.zip 2>/dev/null || true
        ' 2>/dev/null || warning "Nuclei installation failed"
    fi
    
    # Subfinder - subdomain discovery
    if ! check_command subfinder; then
        sudo -u "$SUDO_USER" bash -c '
        curl -sL https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder_linux_amd64.zip -o /tmp/subfinder.zip 2>/dev/null || exit 1
        unzip -q /tmp/subfinder.zip -d ~/.local/bin 2>/dev/null || exit 1
        chmod +x ~/.local/bin/subfinder 2>/dev/null || exit 1
        rm /tmp/subfinder.zip 2>/dev/null || true
        ' 2>/dev/null || warning "Subfinder installation failed"
    fi
    
    # httpx
    if ! check_command httpx; then
        sudo -u "$SUDO_USER" bash -c '
        curl -sL https://github.com/projectdiscovery/httpx/releases/latest/download/httpx_linux_amd64.zip -o /tmp/httpx.zip 2>/dev/null || exit 1
        unzip -q /tmp/httpx.zip -d ~/.local/bin 2>/dev/null || exit 1
        chmod +x ~/.local/bin/httpx 2>/dev/null || exit 1
        rm /tmp/httpx.zip 2>/dev/null || true
        ' 2>/dev/null || warning "HTTPX installation failed"
    fi
    
    success "Web Security Tools installation completed"
}

#====================================================================
# Binary/PWN Tools Installation
#====================================================================

install_binary_tools() {
    info "Installing Binary/PWN Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    sudo apt-get update -qq
    
    # Debuggers
    info "Installing debuggers..."
    sudo apt-get install -y gdb gdb-multiarch > /dev/null 2>&1 || warning "GDB installation failed"
    
    # Disassemblers
    info "Installing disassemblers..."
    sudo apt-get install -y radare2 > /dev/null 2>&1 || warning "radare2 installation failed"
    
    # Download Ghidra (requires manual download for latest version)
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/ghidra" ]; then
        info "Ghidra requires manual download from https://github.com/NationalSecurityAgency/ghidra/releases"
    fi
    
    # Install pwntools
    info "Installing pwntools..."
    pip3 install --quiet pwntools 2>/dev/null || warning "pwntools installation failed"
    
    # ROPGadget
    pip3 install --quiet ROPgadget 2>/dev/null || warning "ROPgadget installation failed"
    
    # one_gadget
    if ! check_command one_gadget; then
        sudo apt-get install -y ruby > /dev/null 2>&1
        sudo gem install one_gadget > /dev/null 2>&1 || warning "one_gadget installation failed"
    fi
    
    # checksec
    info "Installing checksec..."
    if [ ! -f /usr/bin/checksec ]; then
        curl -sL https://github.com/slimm609/checksec.sh/raw/master/checksec -o /tmp/checksec 2>/dev/null || true
        sudo mv /tmp/checksec /usr/bin/checksec 2>/dev/null || true
        sudo chmod +x /usr/bin/checksec 2>/dev/null || true
    fi
    
    # AFL (American Fuzzy Lop)
    info "Installing AFL..."
    sudo apt-get install -y afl++ > /dev/null 2>&1 || warning "AFL installation failed"
    
    success "Binary/PWN Tools installation completed"
}

#====================================================================
# Mobile Security Tools Installation
#====================================================================

install_mobile_tools() {
    info "Installing Mobile Security Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    # Install Android SDK tools (if available)
    info "Installing Android development tools..."
    sudo apt-get install -y default-jdk > /dev/null 2>&1 || warning "JDK installation failed"
    
    # apktool
    if ! check_command apktool; then
        info "Installing apktool..."
        curl -sL https://github.com/iBotPeaches/Apktool/releases/download/v2.7.0/apktool_2.7.0.jar -o /tmp/apktool.jar 2>/dev/null || true
        curl -sL https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -o /tmp/apktool 2>/dev/null || true
        sudo mv /tmp/apktool /usr/local/bin/apktool 2>/dev/null || true
        sudo mv /tmp/apktool.jar /usr/local/bin/apktool.jar 2>/dev/null || true
        sudo chmod +x /usr/local/bin/apktool 2>/dev/null || true
    fi
    
    # jadx - Dex to Java decompiler
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/jadx" ]; then
        git clone --quiet https://github.com/skylot/jadx.git "${WORKSPACE_ROOT}/shared/tools/jadx" 2>/dev/null || warning "jadx clone failed"
    fi
    
    # dex2jar
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/dex2jar" ]; then
        curl -sL https://github.com/pxb1988/dex2jar/releases/download/2.0/dex2jar-2.0.zip -o /tmp/dex2jar.zip 2>/dev/null || true
        unzip -q /tmp/dex2jar.zip -d "${WORKSPACE_ROOT}/shared/tools/" 2>/dev/null || warning "dex2jar extraction failed"
        rm /tmp/dex2jar.zip 2>/dev/null || true
    fi
    
    # Frida
    info "Installing Frida..."
    pip3 install --quiet frida frida-tools 2>/dev/null || warning "Frida installation failed"
    
    # MobSF (requires Docker or manual setup)
    info "MobSF requires manual installation: https://github.com/MobSF/Mobile-Security-Framework-MobSF"
    
    success "Mobile Security Tools installation completed"
}

#====================================================================
# Domain Penetration Tools Installation
#====================================================================

install_domain_tools() {
    info "Installing Domain Penetration Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    # Install impacket
    info "Installing impacket..."
    pip3 install --quiet impacket 2>/dev/null || warning "impacket installation failed"
    
    # BloodHound
    info "Installing BloodHound..."
    if ! check_command bloodhound; then
        # Requires Neo4j database
        info "BloodHound requires Neo4j. Install via: apt install bloodhound"
    fi
    
    # responder
    info "Installing Responder..."
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/Responder" ]; then
        git clone --quiet https://github.com/lgandx/Responder.git "${WORKSPACE_ROOT}/shared/tools/Responder" 2>/dev/null || warning "Responder clone failed"
    fi
    
    # CrackMapExec
    info "Installing CrackMapExec..."
    pip3 install --quiet crackmapexec 2>/dev/null || warning "CrackMapExec installation failed"
    
    # evil-winrm
    if ! check_command evil-winrm; then
        sudo gem install evil-winrm > /dev/null 2>&1 || warning "evil-winrm installation failed"
    fi
    
    # nmap scripts for SMB
    info "Installing Nmap SMB scripts..."
    if [ -d /usr/share/nmap/scripts ]; then
        sudo nmap --script-updatedb > /dev/null 2>&1 || true
    fi
    
    success "Domain Penetration Tools installation completed"
}

#====================================================================
# Anonymity & Proxy Tools Installation
#====================================================================

install_anonymity_tools() {
    info "Installing Anonymity & Proxy Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    sudo apt-get update -qq
    
    # Tor
    info "Installing Tor..."
    sudo apt-get install -y tor > /dev/null 2>&1 || warning "Tor installation failed"
    
    # ProxyChains
    info "Installing ProxyChains..."
    sudo apt-get install -y proxychains proxychains-ng > /dev/null 2>&1 || warning "ProxyChains installation failed"
    
    # Privoxy
    info "Installing Privoxy..."
    sudo apt-get install -y privoxy > /dev/null 2>&1 || warning "Privoxy installation failed"
    
    # netcat
    info "Installing netcat..."
    sudo apt-get install -y netcat-openbsd netcat-traditional > /dev/null 2>&1 || warning "netcat installation failed"
    
    # socat
    info "Installing socat..."
    sudo apt-get install -y socat > /dev/null 2>&1 || warning "socat installation failed"
    
    # openvpn
    info "Installing OpenVPN..."
    sudo apt-get install -y openvpn > /dev/null 2>&1 || warning "OpenVPN installation failed"
    
    # sshuttle
    info "Installing sshuttle..."
    pip3 install --quiet sshuttle 2>/dev/null || warning "sshuttle installation failed"
    
    # macchanger
    info "Installing MAC Changer..."
    sudo apt-get install -y macchanger > /dev/null 2>&1 || warning "macchanger installation failed"
    
    success "Anonymity & Proxy Tools installation completed"
}

#====================================================================
# Blue Team Tools Installation
#====================================================================

install_blueteam_tools() {
    info "Installing Blue Team Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    sudo apt-get update -qq
    
    # Volatility
    info "Installing Volatility..."
    pip3 install --quiet volatility3 2>/dev/null || warning "Volatility installation failed"
    
    # Wireshark
    info "Installing Wireshark..."
    sudo apt-get install -y wireshark tshark > /dev/null 2>&1 || warning "Wireshark installation failed"
    
    # tcpdump
    info "Installing tcpdump..."
    sudo apt-get install -y tcpdump > /dev/null 2>&1 || warning "tcpdump installation failed"
    
    # Suricata
    info "Installing Suricata..."
    sudo apt-get install -y suricata > /dev/null 2>&1 || warning "Suricata installation failed"
    
    # Zeek
    info "Installing Zeek..."
    sudo apt-get install -y zeek > /dev/null 2>&1 || warning "Zeek installation failed"
    
    # YARA
    info "Installing YARA..."
    sudo apt-get install -y yara > /dev/null 2>&1 || warning "YARA installation failed"
    
    # Sleuth Kit / Autopsy
    info "Installing Sleuth Kit..."
    sudo apt-get install -y sleuthkit > /dev/null 2>&1 || warning "Sleuth Kit installation failed"
    
    success "Blue Team Tools installation completed"
}

#====================================================================
# Compliance Tools Installation
#====================================================================

install_compliance_tools() {
    info "Installing Compliance & Recording Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    sudo apt-get update -qq
    
    # Recording tools
    info "Installing recording tools..."
    sudo apt-get install -y ffmpeg > /dev/null 2>&1 || warning "ffmpeg installation failed"
    
    # Terminal recording
    sudo apt-get install -y ttyrec script > /dev/null 2>&1 || warning "ttyrec installation failed"
    
    # asciinema (if available)
    info "Installing asciinema..."
    curl -sL https://asciinema.org/install.sh | sh > /dev/null 2>&1 || warning "asciinema installation failed"
    
    # Hash utilities
    info "Installing hash utilities..."
    sudo apt-get install -y md5deep sha256sum gpg > /dev/null 2>&1 || warning "Hash utilities installation failed"
    
    # auditd
    info "Installing auditd..."
    sudo apt-get install -y auditd > /dev/null 2>&1 || warning "auditd installation failed"
    
    # logrotate
    info "Installing logrotate..."
    sudo apt-get install -y logrotate > /dev/null 2>&1 || warning "logrotate installation failed"
    
    # rsyslog
    info "Installing rsyslog..."
    sudo apt-get install -y rsyslog > /dev/null 2>&1 || warning "rsyslog installation failed"
    
    success "Compliance Tools installation completed"
}

#====================================================================
# Purple Team Tools Installation
#====================================================================

install_purpleteam_tools() {
    info "Installing Purple Team Tools..."
    
    # Atomic Red Team
    info "Installing Atomic Red Team..."
    if [ ! -d "${WORKSPACE_ROOT}/shared/tools/AtomicRedTeam" ]; then
        git clone --quiet https://github.com/redcanaryco/atomic-red-team.git "${WORKSPACE_ROOT}/shared/tools/AtomicRedTeam" 2>/dev/null || warning "Atomic Red Team clone failed"
    fi
    
    # Caldera (requires manual setup)
    info "Caldera requires manual installation: https://github.com/mitre/caldera"
    
    # MITRE ATT&CK navigator
    info "ATT&CK Navigator available at: https://mitre-attack.github.io/attack-navigator/"
    
    # CyberChef
    info "CyberChef available at: https://gchq.github.io/CyberChef/"
    
    success "Purple Team Tools setup info completed"
}

#====================================================================
# General Security Tools Installation
#====================================================================

install_general_tools() {
    info "Installing General Security Tools..."
    
    if ! check_command apt-get; then
        warning "apt-get not found. Skipping."
        return
    fi
    
    sudo apt-get update -qq
    
    # Essential network tools
    info "Installing essential network tools..."
    sudo apt-get install -y \
        nmap \
        masscan \
        net-tools \
        iproute2 \
        dnsutils \
        whois \
        curl \
        wget \
        git \
        vim \
        tmux \
        > /dev/null 2>&1 || warning "Some tools installation failed"
    
    # Python
    info "Installing Python..."
    sudo apt-get install -y python3 python3-pip python3-venv > /dev/null 2>&1 || warning "Python installation failed"
    
    # Docker
    info "Checking Docker..."
    if ! check_command docker; then
        info "Docker not found. Install from: https://docs.docker.com/get-docker/"
    fi
    
    # Virtualization
    info "Installing virtualization tools..."
    sudo apt-get install -y virtualbox qemu-utils > /dev/null 2>&1 || warning "Virtualization tools installation failed"
    
    # Wordlists
    info "Downloading wordlists..."
    mkdir -p "${WORKSPACE_ROOT}/shared/wordlists"
    if [ ! -f "${WORKSPACE_ROOT}/shared/wordlists/rockyou.txt" ]; then
        sudo apt-get install -y wordlists > /dev/null 2>&1 || true
        if [ -f /usr/share/wordlists/rockyou.txt.gz ]; then
            sudo gzip -d /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || true
            sudo cp /usr/share/wordlists/rockyou.txt "${WORKSPACE_ROOT}/shared/wordlists/" 2>/dev/null || true
        fi
    fi
    
    success "General Security Tools installation completed"
}

#====================================================================
# Show Installed Tools
#====================================================================

show_installed() {
    echo ""
    echo "========================================"
    echo "  Installed Tools Status"
    echo "========================================"
    echo ""
    
    tools=(
        "nmap:Nmap"
        "gdb:GDB"
        "python3:Python"
        "pip3:Pip"
        "docker:Docker"
        "wireshark:Wireshark"
        "ffmpeg:FFmpeg"
        "sqlmap:SQLMap"
        "nikto:Nikto"
        "hydra:Hydra"
        "john:John the Ripper"
        "hashcat:Hashcat"
        "metasploit:Metasploit"
        "burpsuite:Burp Suite"
        "radare2:Radare2"
        "frida:Frida"
        "apktool:Apktool"
    )
    
    for tool in "${tools[@]}"; do
        IFS=':' read -r cmd name <<< "$tool"
        if check_command "$cmd"; then
            echo -e "  [${GREEN}✓${NC}] $name"
        else
            echo -e "  [${RED}✗${NC}] $name"
        fi
    done
    
    echo ""
}

#====================================================================
# Main Script
#====================================================================

main() {
    echo ""
    echo "========================================"
    echo "  AI Security Researcher Workspace"
    echo "  Tool Installation Script"
    echo "========================================"
    echo ""
    
    check_root
    
    while true; do
        show_menu
        
        case $choice in
            1) install_web_tools ;;
            2) install_binary_tools ;;
            3) install_mobile_tools ;;
            4) install_domain_tools ;;
            5) install_anonymity_tools ;;
            6) install_blueteam_tools ;;
            7) install_compliance_tools ;;
            8) install_purpleteam_tools ;;
            9) install_general_tools ;;
            10) 
                install_web_tools
                install_binary_tools
                install_mobile_tools
                install_domain_tools
                install_anonymity_tools
                install_blueteam_tools
                install_compliance_tools
                install_purpleteam_tools
                install_general_tools
                success "All tools installation completed!"
                ;;
            11) show_installed ;;
            12) 
                info "Updating package lists..."
                if check_command apt-get; then
                    sudo apt-get update -qq
                    success "Package lists updated"
                fi
                ;;
            0) 
                echo ""
                echo "Goodbye!"
                exit 0
                ;;
            *) 
                echo ""
                echo "Invalid option. Please try again."
                ;;
        esac
        
        echo ""
        read -p "Press Enter to continue..."
    done
}

main

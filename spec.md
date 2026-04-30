
# 专家级渗透测试与安全研究员工作区规划

## 一、检查清单

### 规划阶段检查清单
- [x] 明确工作区目标与使用场景
- [x] 确定红队/蓝队/紫队覆盖范围
- [x] 设计目录架构与文件组织
- [ ] 验证工具清单完整性
- [ ] 设计AI Agent可用的Skills
- [ ] 设计Harness与测试框架

### 实施阶段检查清单
- [ ] 创建基础目录结构
- [ ] 部署核心工具集
- [ ] 配置环境变量与路径
- [ ] 安装依赖库与框架
- [ ] 编写Skills模块
- [ ] 实现Harness框架
- [ ] 配置自动化工作流

### 验证阶段检查清单
- [ ] 测试目录访问权限
- [ ] 验证工具可用性
- [ ] 测试Skills功能
- [ ] 验证Harness执行
- [ ] 执行端到端测试
- [ ] 文档完整性检查

## 二、目录架构

```
pen-test-workspace/
├── README.md
├── .env.example
├── .gitignore
│
├── red-team/                    # 红队攻击场景
│   ├── web-security/           # Web安全
│   │   ├── tools/
│   │   ├── exploits/
│   │   ├── payloads/
│   │   ├── wordlists/
│   │   └── templates/
│   ├── binary-security/        # 二进制安全
│   │   ├── pwn/
│   │   ├── reverse-engineering/
│   │   ├── fuzzing/
│   │   └── debugger/
│   ├── mobile-app/             # 移动应用安全
│   │   ├── android/
│   │   ├── ios/
│   │   └── frida-scripts/
│   ├── miniprogram/            # 微信小程序安全
│   │   ├── unpack/
│   │   ├── audit/
│   │   └── hooks/
│   ├── domain-pentest/         # 域渗透
│   │   ├── enumeration/
│   │   ├── lateral-movement/
│   │   ├── privilege-escalation/
│   │   └── persistence/
│   ├── phishing/               # 钓鱼
│   │   ├── templates/
│   │   ├── payload-generators/
│   │   └── delivery/
│   ├── anonymity/              # 匿名与代理
│   │   ├── proxies/            # 代理工具
│   │   ├── chains/             # 代理链
│   │   ├── tor/                # Tor相关
│   │   ├── i2p/                # I2P相关
│   │   └── vpn/                # VPN配置
│   └── infrastructure/         # 基础设施攻击
│       ├── cloud/
│       ├── network/
│       └── wireless/
│
├── blue-team/                   # 蓝队防御场景
│   ├── incident-response/      # 应急响应
│   │   ├── playbooks/
│   │   ├── forensics/
│   │   ├── malware-analysis/
│   │   └── reporting/
│   ├── threat-intel/           # 威胁情报
│   │   ├── feeds/
│   │   ├── analysis/
│   │   └── indicators/
│   ├── monitoring/             # 监控
│   │   ├── logs/
│   │   ├── alerts/
│   │   └── dashboards/
│   └── hardening/              # 加固
│       ├── benchmarks/
│       ├── checklists/
│       └── scripts/
│
├── purple-team/                 # 紫队协作场景
│   ├── attack-simulation/      # 攻击模拟
│   ├── defense-validation/     # 防御验证
│   ├── forensics/              # 溯源取证
│   │   ├── disk-forensics/
│   │   ├── memory-forensics/
│   │   ├── network-forensics/
│   │   └── timeline/
│   └── training/               # 训练
│
├── compliance/                  # 合规与记录
│   ├── recordings/             # 录屏文件
│   │   ├── screen/             # 屏幕录制
│   │   ├── terminal/           # 终端录制
│   │   └── network/            # 网络流量录制
│   ├── logs/                   # 操作日志
│   │   ├── audit/              # 审计日志
│   │   ├── command/            # 命令日志
│   │   └── session/            # 会话日志
│   ├── evidence/               # 证据管理
│   │   ├── chain-of-custody/   # 证据链
│   │   ├── hashes/             # 文件哈希
│   │   └── signatures/         # 数字签名
│   ├── policies/               # 合规策略
│   └── checklists/             # 合规检查清单
│
├── shared/                      # 共享资源
│   ├── tools/                  # 通用工具
│   ├── wordlists/              # 字典
│   ├── templates/              # 模板
│   ├── datasets/               # 数据集
│   └── documentation/          # 文档
│
├── ai-agent/                    # AI Agent相关
│   ├── skills/                 # Skills模块
│   ├── harness/                # Harness框架
│   ├── prompts/                # 提示词
│   └── workflows/              # 工作流
│
├── config/                      # 配置文件
│   ├── tools/
│   ├── environment/
│   ├── proxy/                  # 代理配置
│   ├── compliance/             # 合规配置
│   └── profiles/
│
└── output/                      # 输出目录
    ├── reports/
    ├── logs/
    ├── artifacts/
    └── screenshots/
```

## 三、工具清单

### 红队工具

#### Web安全
| 工具 | 用途 | 来源 |
|------|------|------|
| Burp Suite | Web应用安全测试 | PortSwigger |
| OWASP ZAP | Web应用安全扫描 | OWASP |
| sqlmap | SQL注入自动化工具 | sqlmap.org |
| XSSer | XSS攻击框架 | xsser.org |
| dirb/dirbuster | 目录爆破 | OWASP |
| gobuster | 目录/DNS爆破 | OJ Reeves |
| wfuzz | Web模糊测试工具 | edge-security.com |
| ffuf | 快速Web模糊器 | ffuf.io |
| nuclei | 漏洞扫描器 | ProjectDiscovery |
| httpx | HTTP工具包 | ProjectDiscovery |
| naabu | 端口扫描器 | ProjectDiscovery |
| subfinder | 子域名发现 | ProjectDiscovery |
| amass | 子域名枚举 | OWASP |
| theHarvester | 信息收集 | laramies/theHarvester |
| wpscan | WordPress扫描器 | wpscan.com |
| droopescan | Drupal扫描器 | droope/droopescan |
| joomscan | Joomla扫描器 | OWASP |
| ysoserial | Java反序列化利用工具 | frohoff/ysoserial |
| ysoserial.net | .NET反序列化利用工具 | pwntester/ysoserial.net |
| JSON Web Token Toolkit | JWT攻击工具 | ticarpi/jwt_tool |

#### 二进制安全/PWN
| 工具 | 用途 | 来源 |
|------|------|------|
| gdb | GNU调试器 | GNU |
| pwndbg | GDB插件 | pwndbg/pwndbg |
| peda | GDB插件 | longld/peda |
| gef | GDB插件 | hugsy/gef |
| IDA Pro | 反汇编器 | Hex-Rays |
| Ghidra | 逆向工程工具 | NSA |
| radare2 | 逆向工程框架 | radareorg/radare2 |
| Binary Ninja | 逆向工程平台 | Vector 35 |
| Hopper | macOS逆向工具 | Hopper |
| pwntools | CTF框架 | Gallopsled/pwntools |
| ropgadget | ROP gadget查找器 | JonathanSalwan/ROPgadget |
| ROPgadget | ROP工具 | shell-storm |
| one_gadget | libc one gadget查找 | david942j/one_gadget |
| checksec | 二进制安全检查 | slimmckee/checksec.sh |
| afl-fuzz | American Fuzzy Lop | lcamtuf/afl |
| libfuzzer | LLVM模糊测试 | LLVM |
| honggfuzz | 模糊测试工具 | google/honggfuzz |
| winAFL | Windows AFL模糊器 | googleprojectzero/winafl |

#### 移动应用安全
| 工具 | 用途 | 来源 |
|------|------|------|
| frida | 动态插桩工具 | frida/frida |
| objection | Frida包装工具 | sensepost/objection |
| apksigner | APK签名工具 | Android |
| apktool | APK反编译工具 | iBotPeaches/Apktool |
| jadx | Dex到Java反编译器 | skylot/jadx |
| dex2jar | Dex转Jar工具 | pxb1988/dex2jar |
| baksmali | Smali反汇编器 | JesusFreke/smali |
| smali | Smali汇编器 | JesusFreke/smali |
| MobSF | 移动安全框架 | MobSF/Mobile-Security-Framework-MobSF |
| drozer | Android安全测试框架 | withsecurelabs/drozer |
| qark | Android安全扫描器 | linkedin/qark |
| needle | iOS安全测试框架 | withsecurelabs/needle |
| frida-scripts | Frida脚本集合 | iddoeldan/frida-scripts |
| frida-code-snippets | Frida代码片段 | fadeevab/frida-code-snippets |

#### 微信小程序安全
| 工具 | 用途 | 来源 |
|------|------|------|
| wxappUnpacker | 小程序反编译工具 | qwerty472123/wxappUnpacker |
| wxapkg | 小程序解包工具 | xuedingmiao/wxapkg |
| wechat_web_devtools | 微信开发者工具 | Tencent |
| miniprogram-decompiler | 小程序反编译 | sysublackbear/wechat-miniprogram-decompiler |
| wxapp-decrypt | 小程序解密工具 | Darkkery/wxapp-decrypt |
| anyproxy | HTTP/HTTPS代理 | alibaba/anyproxy |
| whistle | 调试代理 | avwo/whistle |

#### 域渗透
| 工具 | 用途 | 来源 |
|------|------|------|
| impacket | 网络协议工具集 | SecureAuthCorp/impacket |
| bloodhound | Active Directory可视化 | BloodHoundAD/BloodHound |
| sharphound | BloodHound数据收集器 | BloodHoundAD/BloodHound |
| mimikatz | 凭证提取工具 | gentilkiwi/mimikatz |
| rubeus | Kerberos工具 | GhostPack/Rubeus |
| powerview | PowerShell AD工具 | PowerShellMafia/PowerSploit |
| empire | PowerShell后渗透框架 | EmpireProject/Empire |
| cobalt strike | 商业渗透测试框架 | Strategic Cyber |
| metasploit | 渗透测试框架 | Rapid7 |
| crackmapexec | 后渗透工具 | byt3bl33d3r/CrackMapExec |
| netexec | CrackMapExec后继者 | Pennyw0rth/NetExec |
| evil-winrm | WinRM shell | Hackplayers/evil-winrm |
| proxychains | 代理工具 | haad/proxychains |
| chisel | TCP/UDP隧道工具 | jpillora/chisel |
| ligolo-ng | 隧道工具 | NicoG69/Ligolo-ng |
| socat | 多功能中继工具 | dest-unreach.org/socat |
| plink | PuTTY链接工具 | PuTTY |
| xfreerdp | RDP客户端 | FreeRDP |

#### 钓鱼
| 工具 | 用途 | 来源 |
|------|------|------|
| gophish | 钓鱼框架 | gophish/gophish |
| evilginx2 | 中间人钓鱼框架 | kgretzky/evilginx2 |
| modlishka | 反向代理钓鱼 | drk1wi/Modlishka |
| phishing-frenzy | 钓鱼平台 | pentestgeek/phishing-frenzy |
| king-phisher | 钓鱼工具 | rsmusler/king-phisher |
| social-engineer-toolkit | 社会工程工具包 | trustedsec/social-engineer-toolkit |
| beelogger | 钓鱼键盘记录器 | 4w4k3/BeeLogger |

#### 匿名与代理
| 工具 | 用途 | 来源 |
|------|------|------|
| Tor Browser | 匿名浏览器 | torproject.org |
| tor | Tor守护进程 | torproject.org |
| torsocks | Tor SOCKS代理 | torproject.org |
| torify | 流量Tor化 | torproject.org |
| privoxy | 隐私代理 | privoxy.org |
| proxychains | 代理链工具 | haad/proxychains |
| proxychains-ng | 代理链工具新版 | rofl0r/proxychains-ng |
| shadowsocks | 代理工具 | shadowsocks/shadowsocks |
| shadowsocks-libev | Shadowsocks轻量版 | shadowsocks/shadowsocks-libev |
| v2ray | 网络代理工具 | v2ray/v2ray-core |
| clash | 代理规则工具 | Dreamacro/clash |
| trojan | 代理工具 | trojan-gfw/trojan |
| wireguard | VPN协议 | WireGuard/wireguard-linux |
| openvpn | VPN工具 | OpenVPN/openvpn |
| sshuttle | SSH VPN工具 | sshuttle/sshuttle |
| iodine | DNS隧道工具 | yarrick/iodine |
| dnscat2 | DNS隧道工具 | iagox86/dnscat2 |
| cobalt strike | C2代理功能 | Strategic Cyber |
| ngrok | 内网穿透工具 | ngrok |
| frp | 内网穿透工具 | fatedier/frp |
| chisel | TCP/UDP隧道工具 | jpillora/chisel |
| ligolo-ng | 隧道工具 | NicoG69/Ligolo-ng |
| socat | 多功能中继工具 | dest-unreach.org/socat |
| macchanger | MAC地址修改 | alobbs/macchanger |
| hostapd-mana | 恶意AP工具 | sensepost/hostapd-mana |
| i2p | 匿名网络 | geti2p.net |
| freenet | 匿名网络 | freenetproject.org |

### 蓝队工具

#### 应急响应
| 工具 | 用途 | 来源 |
|------|------|------|
| volatility | 内存取证 | volatilityfoundation/volatility |
| volatility3 | Volatility 3 | volatilityfoundation/volatility3 |
| autopsy | 数字取证平台 | sleuthkit/autopsy |
| sleuthkit | 取证工具库 | sleuthkit/sleuthkit |
| FTK Imager | 取证镜像工具 | AccessData |
| enCase | 取证平台 | OpenText |
| osquery | 操作系统查询 | osquery/osquery |
| velociraptor | 端点监控 | Velocidex/velociraptor |
| sysinternals | Windows工具集 | Microsoft |
| process hacker | 进程查看器 | processhacker/processhacker |
| procmon | 进程监控 | Microsoft |
| autoruns | 启动项检查 | Microsoft |
| tcpview | 网络连接查看 | Microsoft |
| wireshark | 网络协议分析 | Wireshark |
| tcpdump | 网络抓包 | tcpdump |
| tshark | 命令行Wireshark | Wireshark |
| brim | 网络分析工具 | brimdata/brim |
| suricata | IDS/IPS | OISF/suricata |
| zeek | 网络安全监控 | zeek/zeek |
| elasticsearch | 搜索引擎 | Elastic |
| logstash | 日志处理 | Elastic |
| kibana | 数据可视化 | Elastic |
| splunk | 日志分析平台 | Splunk |

#### 威胁情报
| 工具 | 用途 | 来源 |
|------|------|------|
| misp | 威胁情报平台 | MISP/MISP |
| thehive | 安全事件响应平台 | TheHive-Project/TheHive |
| cortex | 分析引擎 | TheHive-Project/Cortex |
| yara | 恶意软件分类 | VirusTotal/yara |
| yarGen | Yara规则生成器 | Neo23x0/yarGen |
| mordor | 威胁数据集 | OTRF/mordor |
| atomic-red-team | 原子测试 | redcanaryco/atomic-red-team |
| attack-navigator | MITRE ATT&amp;CK导航 | mitre-attack/attack-navigator |
| mitre-attack | ATT&amp;CK框架 | mitre/attack |
| threatcrowd | 威胁情报搜索引擎 | AlienVault |
| virus-total | 文件/URL分析 | VirusTotal |
| abuseipdb | IP信誉库 | AbuseIPDB |
| shodan | 搜索引擎 | Shodan |
| censys | 搜索引擎 | Censys |
| binaryedge | 搜索引擎 | BinaryEdge |
| zoomeye | 搜索引擎 | ZoomEye |
| fofa | 搜索引擎 | FOFA |

#### 监控与加固
| 工具 | 用途 | 来源 |
|------|------|------|
| ossec | HIDS | ossec/ossec-hids |
| wazuh | 安全监控平台 | wazuh/wazuh |
| fail2ban | 暴力破解防护 | fail2ban/fail2ban |
| auditd | Linux审计 | Linux |
| sysmon | Windows系统监控 | Microsoft |
| crowdstrike | EDR | CrowdStrike |
| sentinelone | EDR | SentinelOne |
| microsoft defender | EDR | Microsoft |
| palo alto | 防火墙 | Palo Alto |
| snort | IDS/IPS | snort3/snort3 |
| suricata | IDS/IPS | OISF/suricata |
| bro/zeek | 网络分析 | zeek/zeek |
| openscap | 安全合规 | OpenSCAP |
| lynis | 安全审计 | CISOfy/lynis |
| goss | 服务器验证 | goss-org/goss |
| inspec | 合规框架 | inspec/inspec |
| hardening-framework | 加固框架 | various |

#### 合规记录与取证
| 工具 | 用途 | 来源 |
|------|------|------|
| ffmpeg | 屏幕录制 | FFmpeg/FFmpeg |
| obs | 录屏软件 | obsproject/obs-studio |
| simplescreenrecorder | 屏幕录制 | MaartenBaert/ssr |
| vokoscreen | 屏幕录制 | vokoscreen/vokoscreen |
| asciinema | 终端录制 | asciinema/asciinema |
| ttyrec | 终端录制 | mjyc/ttyrec |
| script | 终端会话记录 | Linux |
| screenkey | 按键显示 | wavexx/screenkey |
| tlog | 终端会话记录 | Scribery/tlog |
| auditbeat | 审计日志收集 | elastic/beats |
| filebeat | 日志收集 | elastic/beats |
| tcpdump | 网络抓包 | tcpdump |
| wireshark | 网络协议分析 | Wireshark |
| tshark | 命令行Wireshark | Wireshark |
| tcpflow | TCP流记录 | simsong/tcpflow |
| argus | 网络流量审计 | openargus/argus |
| suricata | IDS/IPS | OISF/suricata |
| zeek | 网络安全监控 | zeek/zeek |
| volatility | 内存取证 | volatilityfoundation/volatility |
| volatility3 | Volatility 3 | volatilityfoundation/volatility3 |
| autopsy | 数字取证平台 | sleuthkit/autopsy |
| sleuthkit | 取证工具库 | sleuthkit/sleuthkit |
| FTK Imager | 取证镜像工具 | AccessData |
| hashdeep | 文件哈希计算 | jessek/hashdeep |
| md5deep | 哈希计算工具 | jessek/hashdeep |
| sha256sum | SHA256哈希计算 | Linux |
| gpg | 加密签名工具 | gnupg/gnupg |
| openssl | 加密工具库 | openssl/openssl |
| logrotate | 日志轮转 | Linux |
| rsyslog | 日志系统 | rsyslog/rsyslog |
| syslog-ng | 日志系统 | syslog-ng/syslog-ng |
| splunk | 日志分析平台 | Splunk |
| elasticsearch | 搜索引擎 | Elastic |
| logstash | 日志处理 | Elastic |
| kibana | 数据可视化 | Elastic |
| grafana | 监控可视化 | grafana/grafana |
| timesketch | 时序取证分析 | google/timesketch |
| tamper-evident | 防篡改日志 | various |

### 紫队工具

| 工具 | 用途 | 来源 |
|------|------|------|
| atomic-red-team | 原子测试 | redcanaryco/atomic-red-team |
| caldera |  adversary emulation | mitre/caldera |
| infection-monkey | 攻击模拟 | guardicore/monkey |
| stratus-red-team | 云攻击模拟 | DataDog/stratus-red-team |
| purple-team-attack-simulator | 紫队模拟器 | various |
| cyberchef | 网络瑞士军刀 | gchq/CyberChef |
| cuckoo sandbox | 沙箱 | cuckoosandbox/cuckoo |
| cape sandbox | 沙箱 | kevoreilly/CAPEv2 |
| any.run | 在线沙箱 | any.run |
| joe sandbox | 沙箱 | joesecurity |
| hybrid-analysis | 沙箱 | Payload Security |
| virustotal sandbox | 沙箱 | VirusTotal |

### 通用工具

| 工具 | 用途 | 来源 |
|------|------|------|
| nmap | 端口扫描 | nmap |
| masscan | 大规模端口扫描 | robertdavidgraham/masscan |
| rustscan | 快速端口扫描 | RustScan/RustScan |
| netcat/ncat | 网络工具 | nmap/nmap |
| curl | 数据传输 | curl/curl |
| wget | 文件下载 | GNU |
| git | 版本控制 | git/git |
| python | 编程语言 | Python |
| ruby | 编程语言 | Ruby |
| go | 编程语言 | Go |
| rust | 编程语言 | Rust |
| powershell | 脚本语言 | Microsoft |
| bash | shell | GNU |
| tmux | 终端复用 | tmux/tmux |
| screen | 终端复用 | GNU |
| vim | 文本编辑 | vim/vim |
| vscode | 代码编辑器 | Microsoft |
| docker | 容器 | docker/docker |
| virtualbox | 虚拟机 | Oracle |
| vmware | 虚拟机 | VMware |
| vagrant | 虚拟机管理 | hashicorp/vagrant |
| ansible | 自动化 | ansible/ansible |
| terraform | IaC | hashicorp/terraform |

## 四、Skills设计

### Red Team Skills

```python
# skills/red_team/web_security.py
class WebSecuritySkill:
    """Web安全测试技能"""

    def scan_target(self, target: str) -&gt; dict:
        """扫描目标Web应用"""
        pass

    def sql_injection_test(self, url: str) -&gt; dict:
        """SQL注入测试"""
        pass

    def xss_test(self, url: str) -&gt; dict:
        """XSS测试"""
        pass

    def directory_bruteforce(self, url: str, wordlist: str) -&gt; list:
        """目录爆破"""
        pass

    def exploit_vulnerability(self, vuln_id: str, target: str) -&gt; dict:
        """利用漏洞"""
        pass
```

```python
# skills/red_team/binary_security.py
class BinarySecuritySkill:
    """二进制安全技能"""

    def analyze_binary(self, binary_path: str) -&gt; dict:
        """分析二进制文件"""
        pass

    def fuzz_binary(self, binary_path: str, iterations: int) -&gt; dict:
        """模糊测试"""
        pass

    def find_rop_gadgets(self, binary_path: str) -&gt; list:
        """查找ROP gadgets"""
        pass

    def generate_exploit(self, binary_path: str, exploit_type: str) -&gt; str:
        """生成Exploit"""
        pass

    def debug_session(self, binary_path: str, commands: list) -&gt; dict:
        """调试会话"""
        pass
```

```python
# skills/red_team/mobile_security.py
class MobileSecuritySkill:
    """移动应用安全技能"""

    def decompile_apk(self, apk_path: str) -&gt; str:
        """反编译APK"""
        pass

    def static_analysis(self, apk_path: str) -&gt; dict:
        """静态分析"""
        pass

    def dynamic_analysis(self, apk_path: str, frida_script: str) -&gt; dict:
        """动态分析"""
        pass

    def hook_function(self, function_name: str, script: str) -&gt; dict:
        """Hook函数"""
        pass

    def extract_secrets(self, apk_path: str) -&gt; dict:
        """提取敏感信息"""
        pass
```

```python
# skills/red_team/domain_pentest.py
class DomainPentestSkill:
    """域渗透技能"""

    def enumerate_domain(self, domain: str) -&gt; dict:
        """枚举域信息"""
        pass

    def dump_credentials(self, target: str) -&gt; dict:
        """转储凭证"""
        pass

    def lateral_movement(self, source: str, target: str) -&gt; dict:
        """横向移动"""
        pass

    def escalate_privileges(self, target: str) -&gt; dict:
        """权限提升"""
        pass

    def establish_persistence(self, target: str, method: str) -&gt; dict:
        """建立持久化"""
        pass
```

```python
# skills/red_team/anonymity.py
class AnonymitySkill:
    """匿名与代理技能"""

    def setup_tor(self, config: dict) -&gt; dict:
        """配置Tor"""
        pass

    def setup_proxy_chain(self, proxies: list) -&gt; dict:
        """配置代理链"""
        pass

    def setup_vpn(self, config: dict) -&gt; dict:
        """配置VPN"""
        pass

    def change_mac_address(self, interface: str, mac: str = None) -&gt; dict:
        """修改MAC地址"""
        pass

    def setup_tunnel(self, type: str, config: dict) -&gt; dict:
        """配置隧道"""
        pass

    def route_traffic(self, tool: str, proxy: str) -&gt; dict:
        """路由工具流量"""
        pass

    def check_anonymity(self) -&gt; dict:
        """检查匿名状态"""
        pass
```

### Blue Team Skills

```python
# skills/blue_team/incident_response.py
class IncidentResponseSkill:
    """应急响应技能"""

    def triage_incident(self, incident_data: dict) -&gt; dict:
        """事件分类"""
        pass

    def collect_evidence(self, target: str) -&gt; dict:
        """收集证据"""
        pass

    def analyze_memory_dump(self, dump_path: str) -&gt; dict:
        """分析内存转储"""
        pass

    def analyze_logs(self, log_paths: list) -&gt; dict:
        """分析日志"""
        pass

    def generate_report(self, findings: dict) -&gt; str:
        """生成报告"""
        pass
```

```python
# skills/blue_team/threat_intel.py
class ThreatIntelSkill:
    """威胁情报技能"""

    def search_ioc(self, ioc: str) -&gt; dict:
        """搜索IOC"""
        pass

    def enrich_data(self, data: dict) -&gt; dict:
        """数据富集"""
        pass

    def generate_yara_rule(self, sample_path: str) -&gt; str:
        """生成Yara规则"""
        pass

    def correlate_incidents(self, incidents: list) -&gt; dict:
        """关联事件"""
        pass

    def track_actor(self, actor_id: str) -&gt; dict:
        """追踪威胁行为者"""
        pass
```

### Purple Team Skills

```python
# skills/purple_team/forensics.py
class ForensicsSkill:
    """溯源取证技能"""

    def analyze_disk_image(self, image_path: str) -&gt; dict:
        """分析磁盘镜像"""
        pass

    def recover_deleted_files(self, image_path: str) -&gt; list:
        """恢复删除文件"""
        pass

    def build_timeline(self, evidence_paths: list) -&gt; dict:
        """构建时间线"""
        pass

    def analyze_network_traffic(self, pcap_path: str) -&gt; dict:
        """分析网络流量"""
        pass

    def trace_attribution(self, evidence: dict) -&gt; dict:
        """追踪归因"""
        pass
```

```python
# skills/purple_team/attack_simulation.py
class AttackSimulationSkill:
    """攻击模拟技能"""

    def run_atomic_test(self, test_id: str, target: str) -&gt; dict:
        """运行原子测试"""
        pass

    def simulate_attack(self, scenario: str, target: str) -&gt; dict:
        """模拟攻击"""
        pass

    def validate_defense(self, attack_result: dict, defense_config: dict) -&gt; dict:
        """验证防御"""
        pass

    def generate_assessment(self, simulation_data: dict) -&gt; dict:
        """生成评估"""
        pass
```

### General Skills

```python
# skills/general/tools.py
class ToolsSkill:
    """通用工具技能"""

    def run_nmap(self, target: str, flags: str) -&gt; dict:
        """运行Nmap扫描"""
        pass

    def execute_command(self, command: str, timeout: int) -&gt; dict:
        """执行命令"""
        pass

    def parse_tool_output(self, tool: str, output: str) -&gt; dict:
        """解析工具输出"""
        pass
```

```python
# skills/general/reporting.py
class ReportingSkill:
    """报告生成技能"""

    def generate_pentest_report(self, findings: list) -&gt; str:
        """生成渗透测试报告"""
        pass

    def create_executive_summary(self, data: dict) -&gt; str:
        """创建执行摘要"""
        pass

    def export_findings(self, findings: list, format: str) -&gt; str:
        """导出发现"""
        pass
```

```python
# skills/compliance/recording.py
class RecordingSkill:
    """记录与录制技能"""

    def start_screen_recording(self, output_path: str, config: dict) -&gt; str:
        """开始屏幕录制"""
        pass

    def stop_screen_recording(self, recording_id: str) -&gt; dict:
        """停止屏幕录制"""
        pass

    def start_terminal_recording(self, output_path: str) -&gt; str:
        """开始终端录制"""
        pass

    def stop_terminal_recording(self, recording_id: str) -&gt; dict:
        """停止终端录制"""
        pass

    def start_network_capture(self, output_path: str, filter: str) -&gt; str:
        """开始网络抓包"""
        pass

    def stop_network_capture(self, capture_id: str) -&gt; dict:
        """停止网络抓包"""
        pass

    def enable_audit_logging(self, config: dict) -&gt; dict:
        """启用审计日志"""
        pass
```

```python
# skills/compliance/evidence.py
class EvidenceSkill:
    """证据管理技能"""

    def generate_hash(self, file_path: str, algorithm: str = "sha256") -&gt; str:
        """生成文件哈希"""
        pass

    def verify_hash(self, file_path: str, expected_hash: str) -&gt; bool:
        """验证文件哈希"""
        pass

    def sign_file(self, file_path: str, key_path: str) -&gt; str:
        """签名文件"""
        pass

    def verify_signature(self, file_path: str, signature_path: str, key_path: str) -&gt; bool:
        """验证签名"""
        pass

    def create_chain_of_custody(self, evidence: dict) -&gt; dict:
        """创建证据链"""
        pass

    def update_chain_of_custody(self, custody_id: str, action: str, actor: str) -&gt; dict:
        """更新证据链"""
        pass

    def seal_evidence(self, evidence_path: str, output_path: str) -&gt; str:
        """封存证据"""
        pass

    def create_forensic_image(self, source: str, output_path: str) -&gt; str:
        """创建取证镜像"""
        pass
```

```python
# skills/compliance/compliance.py
class ComplianceSkill:
    """合规检查技能"""

    def run_compliance_check(self, standard: str) -&gt; dict:
        """运行合规检查"""
        pass

    def generate_compliance_report(self, findings: dict) -&gt; str:
        """生成合规报告"""
        pass

    def verify_evidence_integrity(self, evidence_list: list) -&gt; dict:
        """验证证据完整性"""
        pass

    def check_log_integrity(self, log_paths: list) -&gt; dict:
        """检查日志完整性"""
        pass

    def archive_session(self, session_id: str, output_path: str) -&gt; dict:
        """归档会话"""
        pass
```

## 五、Harness设计

### Web安全测试Harness

```python
# harness/web_security_harness.py
class WebSecurityHarness:
    """Web安全测试Harness"""

    def __init__(self, config: dict):
        self.config = config
        self.target = config.get('target')
        self.results = []

    def run_full_scan(self):
        """运行完整扫描流程"""
        pass

    def test_sqli(self):
        """测试SQL注入"""
        pass

    def test_xss(self):
        """测试XSS"""
        pass

    def test_csrf(self):
        """测试CSRF"""
        pass

    def test_ssrf(self):
        """测试SSRF"""
        pass

    def test_lfi_rfi(self):
        """测试LFI/RFI"""
        pass

    def get_results(self):
        """获取结果"""
        return self.results
```

### 二进制安全Harness

```python
# harness/binary_harness.py
class BinaryHarness:
    """二进制安全Harness"""

    def __init__(self, binary_path: str, config: dict):
        self.binary_path = binary_path
        self.config = config
        self.crashes = []

    def fuzz(self, iterations: int = 1000):
        """模糊测试"""
        pass

    def analyze_crash(self, crash_input: bytes):
        """分析崩溃"""
        pass

    def generate_exploit_template(self, crash_info: dict):
        """生成Exploit模板"""
        pass

    def verify_exploit(self, exploit: str):
        """验证Exploit"""
        pass
```

### 域渗透Harness

```python
# harness/domain_harness.py
class DomainPentestHarness:
    """域渗透Harness"""

    def __init__(self, domain_config: dict):
        self.domain = domain_config.get('domain')
        self.username = domain_config.get('username')
        self.password = domain_config.get('password')
        self.loot = {}

    def reconnaissance(self):
        """侦察阶段"""
        pass

    def initial_access(self):
        """初始访问"""
        pass

    def privilege_escalation(self):
        """权限提升"""
        pass

    def lateral_movement(self):
        """横向移动"""
        pass

    def persistence(self):
        """持久化"""
        pass

    def collection(self):
        """收集"""
        pass

    def exfiltration(self):
        """渗出"""
        pass
```

### 应急响应Harness

```python
# harness/incident_response_harness.py
class IncidentResponseHarness:
    """应急响应Harness"""

    def __init__(self, incident_config: dict):
        self.incident_id = incident_config.get('incident_id')
        self.evidence = []
        self.timeline = []

    def preparation(self):
        """准备阶段"""
        pass

    def identification(self):
        """识别阶段"""
        pass

    def containment(self):
        """遏制阶段"""
        pass

    def eradication(self):
        """根除阶段"""
        pass

    def recovery(self):
        """恢复阶段"""
        pass

    def lessons_learned(self):
        """经验总结"""
        pass
```

### 取证分析Harness

```python
# harness/forensics_harness.py
class ForensicsHarness:
    """取证分析Harness"""

    def __init__(self, case_config: dict):
        self.case_id = case_config.get('case_id')
        self.artifacts = []
        self.timeline = []

    def acquire_evidence(self, source: str, type: str):
        """获取证据"""
        pass

    def validate_integrity(self, evidence_path: str):
        """验证完整性"""
        pass

    def process_artifacts(self):
        """处理人工制品"""
        pass

    def build_timeline(self):
        """构建时间线"""
        pass

    def correlate_events(self):
        """关联事件"""
        pass

    def generate_report(self):
        """生成报告"""
        pass
```

### 通用测试Harness

```python
# harness/generic_harness.py
class GenericHarness:
    """通用测试Harness"""

    def __init__(self, config: dict):
        self.config = config
        self.state = 'initialized'
        self.logs = []

    def setup(self):
        """设置"""
        pass

    def execute(self):
        """执行"""
        pass

    def teardown(self):
        """清理"""
        pass

    def validate(self):
        """验证"""
        pass

    def run_workflow(self, workflow: list):
        """运行工作流"""
        pass
```

### 匿名与代理Harness

```python
# harness/anonymity_harness.py
class AnonymityHarness:
    """匿名与代理Harness"""

    def __init__(self, config: dict):
        self.config = config
        self.active_proxies = []
        self.active_vpn = None
        self.anonymity_level = 0

    def setup_tor_network(self):
        """配置Tor网络"""
        pass

    def setup_proxy_chain(self, proxy_list: list):
        """配置代理链"""
        pass

    def connect_vpn(self, vpn_config: dict):
        """连接VPN"""
        pass

    def disconnect_vpn(self):
        """断开VPN"""
        pass

    def anonymize_system(self):
        """系统匿名化"""
        pass

    def check_ip_leak(self):
        """检查IP泄露"""
        pass

    def check_dns_leak(self):
        """检查DNS泄露"""
        pass

    def get_current_ip_info(self):
        """获取当前IP信息"""
        pass

    def route_tool_traffic(self, tool_name: str):
        """路由工具流量"""
        pass

    def cleanup(self):
        """清理匿名配置"""
        pass
```

### 合规记录Harness

```python
# harness/compliance_harness.py
class ComplianceHarness:
    """合规记录Harness"""

    def __init__(self, session_config: dict):
        self.session_id = session_config.get('session_id')
        self.start_time = None
        self.end_time = None
        self.recordings = {}
        self.evidence = {}
        self.chain_of_custody = []
        self.audit_log = []

    def start_session(self):
        """开始会话"""
        pass

    def start_all_recordings(self):
        """开始所有录制"""
        pass

    def stop_all_recordings(self):
        """停止所有录制"""
        pass

    def collect_evidence(self, source: str, type: str):
        """收集证据"""
        pass

    def document_action(self, action: str, details: dict):
        """记录操作"""
        pass

    def verify_evidence_integrity(self):
        """验证证据完整性"""
        pass

    def create_compliance_report(self):
        """创建合规报告"""
        pass

    def create_chain_of_custody_report(self):
        """创建证据链报告"""
        pass

    def seal_session_evidence(self):
        """封存会话证据"""
        pass

    def archive_session(self, output_path: str):
        """归档会话"""
        pass

    def end_session(self):
        """结束会话"""
        pass
```

### 渗透测试会话Harness

```python
# harness/session_harness.py
class SessionHarness:
    """渗透测试会话Harness"""

    def __init__(self, config: dict):
        self.config = config
        self.session_id = None
        self.anonymity_harness = None
        self.compliance_harness = None
        self.web_harness = None
        self.domain_harness = None

    def initialize(self):
        """初始化会话"""
        pass

    def setup_anonymity(self, anonymity_config: dict):
        """配置匿名环境"""
        pass

    def start_compliance_recording(self):
        """开始合规记录"""
        pass

    def execute_test(self, test_config: dict):
        """执行测试"""
        pass

    def pause_compliance_recording(self):
        """暂停合规记录"""
        pass

    def resume_compliance_recording(self):
        """恢复合规记录"""
        pass

    def complete_test(self):
        """完成测试"""
        pass

    def finalize_session(self):
        """完成会话"""
        pass

    def generate_final_report(self):
        """生成最终报告"""
        pass
```

## 六、工作流示例

### Web渗透测试工作流

```yaml
# workflows/web_pentest.yml
name: Web Penetration Test
stages:
  - name: Reconnaissance
    skills:
      - WebSecuritySkill.scan_target
      - ToolsSkill.run_nmap
  - name: Vulnerability Assessment
    skills:
      - WebSecuritySkill.directory_bruteforce
      - WebSecuritySkill.sql_injection_test
      - WebSecuritySkill.xss_test
  - name: Exploitation
    skills:
      - WebSecuritySkill.exploit_vulnerability
  - name: Reporting
    skills:
      - ReportingSkill.generate_pentest_report
```

### 应急响应工作流

```yaml
# workflows/incident_response.yml
name: Incident Response
stages:
  - name: Preparation
    skills:
      - IncidentResponseSkill.triage_incident
  - name: Identification
    skills:
      - IncidentResponseSkill.collect_evidence
      - ThreatIntelSkill.search_ioc
  - name: Containment
    skills:
      - IncidentResponseSkill.analyze_logs
  - name: Eradication
    skills:
      - IncidentResponseSkill.analyze_memory_dump
  - name: Recovery
    skills:
      - ReportingSkill.generate_report
```

### 取证分析工作流

```yaml
# workflows/forensics.yml
name: Forensic Analysis
stages:
  - name: Evidence Acquisition
    skills:
      - ForensicsSkill.acquire_evidence
      - ForensicsSkill.validate_integrity
  - name: Artifact Processing
    skills:
      - ForensicsSkill.process_artifacts
  - name: Timeline Building
    skills:
      - ForensicsSkill.build_timeline
      - ForensicsSkill.correlate_events
  - name: Reporting
    skills:
      - ForensicsSkill.generate_report
```

### 完整渗透测试会话工作流

```yaml
# workflows/full_pentest_session.yml
name: Full Penetration Test Session
stages:
  - name: Session Initialization
    skills:
      - SessionHarness.initialize
      - ComplianceHarness.start_session
  - name: Anonymity Setup
    skills:
      - AnonymitySkill.setup_tor
      - AnonymitySkill.setup_proxy_chain
      - AnonymitySkill.check_anonymity
      - ComplianceHarness.start_all_recordings
  - name: Reconnaissance
    skills:
      - WebSecuritySkill.scan_target
      - ToolsSkill.run_nmap
  - name: Vulnerability Assessment
    skills:
      - WebSecuritySkill.directory_bruteforce
      - WebSecuritySkill.sql_injection_test
  - name: Exploitation
    skills:
      - WebSecuritySkill.exploit_vulnerability
      - EvidenceSkill.generate_hash
      - EvidenceSkill.create_chain_of_custody
  - name: Post-Exploitation
    skills:
      - DomainPentestSkill.lateral_movement
      - EvidenceSkill.collect_evidence
  - name: Reporting
    skills:
      - ReportingSkill.generate_pentest_report
      - ComplianceSkill.generate_compliance_report
  - name: Session Completion
    skills:
      - ComplianceHarness.stop_all_recordings
      - ComplianceHarness.seal_session_evidence
      - AnonymityHarness.cleanup
      - SessionHarness.finalize_session
```

### 匿名测试工作流

```yaml
# workflows/anonymity_test.yml
name: Anonymity Test
stages:
  - name: Start Compliance Recording
    skills:
      - RecordingSkill.start_screen_recording
      - RecordingSkill.start_terminal_recording
  - name: Configure Anonymity
    skills:
      - AnonymitySkill.setup_tor
      - AnonymitySkill.change_mac_address
      - AnonymitySkill.setup_proxy_chain
  - name: Test Anonymity
    skills:
      - AnonymitySkill.check_anonymity
      - AnonymityHarness.check_ip_leak
      - AnonymityHarness.check_dns_leak
  - name: Test Tools Routing
    skills:
      - AnonymitySkill.route_traffic
  - name: Complete and Archive
    skills:
      - RecordingSkill.stop_screen_recording
      - RecordingSkill.stop_terminal_recording
      - EvidenceSkill.generate_hash
      - ComplianceSkill.archive_session
```

## 七、配置文件示例

### 环境配置

```bash
# config/environment/.env.example
# 路径配置
WORKSPACE_ROOT=/opt/pen-test-workspace
TOOLS_PATH=${WORKSPACE_ROOT}/shared/tools
WORDLISTS_PATH=${WORKSPACE_ROOT}/shared/wordlists
OUTPUT_PATH=${WORKSPACE_ROOT}/output
COMPLIANCE_PATH=${WORKSPACE_ROOT}/compliance
PROXY_CONFIG_PATH=${WORKSPACE_ROOT}/config/proxy

# API密钥
VIRUSTOTAL_API_KEY=your_api_key_here
SHODAN_API_KEY=your_api_key_here
CENSYS_API_ID=your_api_id_here
CENSYS_API_SECRET=your_api_secret_here

# 数据库配置
DATABASE_URL=sqlite:///data/pentest.db

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=${OUTPUT_PATH}/logs/workspace.log

# 代理配置
TOR_ENABLED=true
TOR_SOCKS_PORT=9050
TOR_CONTROL_PORT=9051
PROXYCHAINS_ENABLED=true

# 合规配置
RECORDING_ENABLED=true
SCREEN_RECORDING_ENABLED=true
TERMINAL_RECORDING_ENABLED=true
NETWORK_CAPTURE_ENABLED=false
AUDIT_LOGGING_ENABLED=true
EVIDENCE_SIGNING_ENABLED=true
ENCRYPTION_ENABLED=true

# GPG配置
GPG_KEY_ID=your_key_id
GPG_KEY_PATH=/path/to/private/key

# 会话配置
SESSION_AUTO_START=true
SESSION_AUTO_ARCHIVE=true
SESSION_RENTENTION_DAYS=90
```

### 工具配置

```yaml
# config/tools/nmap.yml
default_flags: -sV -sC -p-
script_path: /usr/share/nmap/scripts
output_format: xml
```

```yaml
# config/tools/burpsuite.yml
api_url: http://127.0.0.1:1337
api_key: your_api_key
targets: []
```

### 代理配置

```yaml
# config/proxy/tor.yml
enabled: true
socks_port: 9050
control_port: 9051
control_password: your_control_password
exit_nodes: []
entry_nodes: []
```

```yaml
# config/proxy/proxychains.yml
enabled: true
chain_type: dynamic
proxy_dns: true
proxies:
  - type: socks5
    host: 127.0.0.1
    port: 9050
  - type: http
    host: proxy.example.com
    port: 8080
```

```yaml
# config/proxy/vpn.yml
providers:
  - name: vpn1
    type: openvpn
    config_path: /etc/openvpn/vpn1.ovpn
  - name: vpn2
    type: wireguard
    config_path: /etc/wireguard/wg0.conf
```

### 合规配置

```yaml
# config/compliance/recording.yml
screen_recording:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/screen
  format: mp4
  fps: 30
  audio: true

terminal_recording:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/terminal
  format: cast

network_capture:
  enabled: true
  output_directory: ${COMPLIANCE_PATH}/recordings/network
  format: pcap
  filter: "not port 22"

audit_logging:
  enabled: true
  log_directory: ${COMPLIANCE_PATH}/logs/audit
  include_commands: true
  include_network: true
  include_file_access: true
```

```yaml
# config/compliance/evidence.yml
hash_algorithm: sha256
sign_evidence: true
gpg_key_path: /path/to/gpg/key
chain_of_custody:
  enabled: true
  auto_document: true
  require_actor: true

retention:
  active: 90
  archived: 365

encryption:
  enabled: true
  algorithm: aes-256-gcm
```

```yaml
# config/compliance/session.yml
session:
  auto_start: true
  auto_stop: true
  auto_archive: true

pre_session_checklist:
  - verify_authorization
  - check_anonymity_settings
  - test_recording_tools
  - confirm_target_scope

post_session_checklist:
  - verify_all_recordings
  - generate_hashes
  - seal_evidence
  - create_report
  - archive_session
```

## 八、合规规范

### 授权验证

- **每次测试前必须验证授权**
- 保存书面授权文件
- 确认测试范围和边界
- 记录授权人和时间

### 会话记录要求

- **强制屏幕录制**
- **强制终端会话记录**
- **可选网络流量捕获**
- 所有记录带时间戳
- 记录包含操作人信息

### 证据管理规范

- 所有收集的证据必须生成哈希
- 重要证据需要数字签名
- 维护完整的证据链
- 证据处理操作必须记录
- 证据访问控制

### 数据保护规范

- 避免在日志中记录明文凭证
- 敏感数据需要加密存储
- 测试完成后清理敏感数据
- 遵守数据最小化原则
- 数据保留政策执行

### 合规检查清单

- [ ] 授权文件已验证
- [ ] 屏幕录制已启动
- [ ] 终端录制已启动
- [ ] 审计日志已启用
- [ ] 匿名配置已确认
- [ ] 测试范围已确认
- [ ] 证据哈希已生成
- [ ] 证据链已创建
- [ ] 最终报告已生成
- [ ] 会话已安全归档

### 合规标准参考

- OWASP 渗透测试标准
- PTES (渗透测试执行标准)
- NIST SP 800-115
- ISO 27001
- 当地法律法规要求

## 九、使用指南

### 快速开始

1. 克隆工作区仓库
2. 配置环境变量（复制.env.example到.env）
3. 安装依赖工具
4. 配置代理和匿名设置
5. 配置合规录制选项
6. 运行初始化脚本
7. 开始使用

### 渗透测试会话流程

1. **会话初始化**
   - 验证授权
   - 配置工作区
   - 生成会话ID

2. **匿名配置**
   - 配置Tor/代理
   - 修改MAC地址
   - 验证匿名性

3. **开始录制**
   - 启动屏幕录制
   - 启动终端录制
   - 启动网络捕获
   - 启用审计日志

4. **执行测试**
   - 执行预定测试用例
   - 记录发现和证据
   - 生成证据哈希

5. **完成测试**
   - 停止所有录制
   - 验证证据完整性
   - 创建证据链
   - 生成测试报告

6. **归档会话**
   - 加密敏感数据
   - 打包所有证据
   - 数字签名
   - 安全存储

### AI Agent集成

1. 将skills目录添加到Agent的技能路径
2. 配置harness框架
3. 加载工作流定义
4. 配置合规和代理设置
5. 执行任务

### 最佳实践

- 保持工具更新
- 使用版本控制管理payloads和exploits
- 定期备份输出和报告
- 每次测试前验证授权
- 始终启用合规录制
- 定期检查和更新匿名配置
- 遵循道德准则和法律法规
- 定期进行合规审计

## 十、法律与道德声明

本工作区仅用于授权的安全测试、研究和教育目的。使用者必须：
- 获得明确的书面授权
- 遵守适用的法律法规
- 不造成不必要的损害
- 及时报告发现的漏洞

任何未经授权的使用均严格禁止，使用者需自行承担相应责任。


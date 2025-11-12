# FCFS NFT Minter  
**First Come First Served NFT Minting Script**  
Supports **Ethereum** & **Solana** with **Wallet Connect** — **No Private Key Needed!**

---

## Features
- Wallet Connect (MetaMask / Phantom)
- FCFS Auto-Mint with Retry
- Testnet Ready (Goerli / Devnet)
- 100% Safe & Local
- Gas Optimization (ETH) | Priority Fee (Solana)

---

## Folder Structure
fcfs-nft-minter/
├── eth/             → Ethereum Script
├── solana/          → Solana Script
├── test/            → Test Contract
├── .gitignore       → Hides .env
├── README.md        → This file
├── package.json     → Node.js deps
└── requirements.txt → Python deps


---

## Setup (Browser Only)

### 1. Download Project
Click **"Code" → "Download ZIP"**

### 2. Install Dependencies (No Code!)

#### For Ethereum (Python)
1. Open folder → Open `requirements.txt`
2. Copy all lines
3. Go to: [https://webpip.vercel.app](https://webpip.vercel.app)
4. Paste → Click **"Install"** → Download `.whl` files
5. (Optional) Use locally later

#### For Solana (Node.js)
1. Go to: [https://www.npmjs.com/package/@metaplex-foundation/js](https://www.npmjs.com/package/@metaplex-foundation/js)
2. Click **"Install"** → Copy command
3. (Use in VS Code later)

---

## Testing (Testnet First!)

### Ethereum (Goerli)
1. Get free ETH: [goerlifaucet.com](https://goerlifaucet.com)
2. Deploy `test/test_contract.sol` on [Remix](https://remix.ethereum.org)
3. Run script → Connect MetaMask → Mint!

### Solana (Devnet)
1. Phantom → Switch to **Devnet**
2. Get free SOL: Terminal → `solana airdrop 2`
3. Run script → Connect Phantom → Mint!

---

## Mainnet Switch
1. Change RPC in script:
   - ETH → Alchemy/Infura
   - Solana → `mainnet-beta`
2. Paste real **contract address**
3. Script will auto-wait for sale!

---

## Safety
- No private key in code
- `.env` ignored
- Testnet = 0 risk

---

## Scripts
| Chain | File |
|-------|------|
| ETH   | `eth/mint_eth_wallet.py` |
| Solana| `solana/mint_solana_wallet.js` |

---

## Author
**Bybit Baba**  
GitHub: [@bybibaba](https://github.com/bybitbaba)

---

> **FCFS mein koi nahi rok sakta!**  
> **Mint. Win. Repeat.**

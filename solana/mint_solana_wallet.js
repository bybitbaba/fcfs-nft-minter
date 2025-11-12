// solana/mint_solana_wallet.js - Solana FCFS Minter (Phantom Connect)
const { Connection, PublicKey } = require('@solana/web3.js');
const { Metaplex } = require('@metaplex-foundation/js');

const connection = new Connection('https://api.devnet.solana.com', 'confirmed');  // Mainnet: 'https://api.mainnet-beta.solana.com'
const CANDY_MACHINE_ID = process.env.CANDY_ID || 'YourCandyMachineID';  // Set in .env

async function connectPhantom() {
    if (typeof window !== 'undefined' && window.solana) {
        try {
            await window.solana.connect();
            console.log('Connected to:', window.solana.publicKey.toString());
            return window.solana;
        } catch (err) {
            console.error('Phantom connect failed:', err);
        }
    } else {
        console.log('Install Phantom Wallet & Refresh');
    }
}

async function mintNFT() {
    const wallet = await connectPhantom();
    if (!wallet) return;

    const metaplex = Metaplex.make(connection).use(walletAdapterIdentity(wallet));

    try {
        const candyMachine = await metaplex.candyMachines().findByAddress({ address: new PublicKey(CANDY_MACHINE_ID) });
        const { nft } = await metaplex.candyMachines().mint({ candyMachine });
        console.log('Minted NFT:', nft.address.toString());
    } catch (error) {
        console.error('Mint failed:', error);
    }
}

// FCFS Auto-Retry
console.log('FCFS Mode: Starting monitor...');
setInterval(async () => {
    try {
        await mintNFT();
    } catch (e) {
        console.log('Retry in 1s...', e.message);
    }
}, 1000);

// For Node.js run: node mint_solana_wallet.js (use browser for full Phantom)
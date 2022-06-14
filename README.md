# Solidity_Python_Projects
Deploying solidity contracts to various testnets and local environments, using python for deployments. 

## Pre-requeisites 

### Brownie Introduction
- Some Users:
  - https://yearn.finance/
  - https://curve.fi/
  - https://badger.finance/
### Installing Brownie
- [Installing Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
  - Install pipx
  - pipx install eth-brownie
  - Testing Successful Install
### Brownie Simple Storage Project
- A new Brownie project with `brownie init`
  - Project Basic Explanation
- Adding `SimpleStorage.sol` to the `contracts` folder
- Compiling with `brownie compile`
- Brownie deploy script
  - `def main` is brownie's entry point
- brownie defaults to a `development` `ganache` chain that it creates
- Placing functions outside of the `main` function
- brownie `accounts`
  - 3 Ways to Add Accounts
    1. `accounts[0]`: Brownie's "default" ganache accounts
       - Only works for local ganache 
    2. `accounts.load("...")`: Brownie's encrypted command line (MOST SECURE)
       - Run `brownie accounts new <name>` and enter your private key and a password
    3. `accounts.add(config["wallets"]["from_key"])`: Storing Private Keys as an environment variable, and pulling from our `brownie-config.yaml`
        - You'll need to add `dotenv: .env` to your `brownie-config.yaml` and have a `.env` file
- Importing a Contract
- Contract.Deploy
- View Function Call in Brownie
- State-Changing Function Call in Brownie / Contract Interaction
- `transaction.wait(1)`
### Testing Basics
- `test_simple_storage.py`
- Arrange, Act, Assert
- [`assert`](https://docs.pytest.org/en/6.2.x/assert.html)
- `brownie test`
- `test_updating_storage`
- [Pytest / Brownie Test Tips](https://docs.pytest.org/en/6.2.x/)
- Deploy to a Testnet
- `brownie networks list`
- Development vs Ethereum
  - Development is temporary
  - Ethereum networks persist
- RPC URL / HTTP Provider in Brownie
- The network flag
  - `list index out of range`
- `get_account()`
- `networks.show_active()`
- build/deployments
- Accessing previous deployments
- Interacting with contracts deployed in our brownie project
### [Brownie console]
- `brownie console`

# SmartContract Lottery

[Chainlink VRF v1 docs](https://docs.chain.link/docs/get-a-random-number/v1/)

### Introduction
- Add a `README.md`
- Defining the project
- Is it decentralized?
### `Lottery.sol`
- basic setup
- Main Functions
- address payable[]
- getEntranceFee & Setup
  - [Chainlink Price Feed](https://docs.chain.link/docs/get-the-latest-price/)
  - brownie-config
  - SPDX
- Matching Units of Measure
  - Can't just divide
- Test early and often
- Quick Math Sanity Check
- deleting networks
- [Alchemy](https://www.alchemy.com/) again
- Enum
- `startLottery`
- [Openzeppelin](https://openzeppelin.com/contracts/)... Is this the first openzeppelin reference? 
- [Openzeppelin Contracts Github](https://github.com/OpenZeppelin/openzeppelin-contracts)
- Randomness
- Pseudorandomness
- `block` keyword
  - `block.difficulty`
  - `block.timestamp`
- `keccack256`
- [True Randomness with Chainlink VRF](https://docs.chain.link/docs/get-a-random-number/)
- Chainlink VRF Remix Version
- Inheriting Constructors
- Oracle Gas & Transaction Gas
- [Why didn't we pay gas on the price feeds?](https://ethereum.stackexchange.com/questions/87473/is-chainlinks-price-reference-data-free-to-consume)
- Chainlink Node Fees
- [Request And Receive Introduction](https://docs.chain.link/docs/architecture-request-model/)
- [Kovan Faucets](https://docs.chain.link/docs/link-token-contracts/#kovan)
- Funding Chainlink Contracts
- [Request And Receive Explanation](https://docs.chain.link/docs/architecture-request-model/)
- A Clarification
- `endLottery`
- `returns (type variableName)`
- `fulfillRandomness`
- `override`
- Modulo Operation (Mod Operation %)
- Paying the lottery winner
- Resetting the lottery
### Testing Lottery.sol
- `deploy_lottery.py`
- `get_account()` refactored
- `get_contract`
  - `contract_to_mock`
  - `Contract.from_abi`
- Adding the parameters to deploying to lottery
- `vrfCoordinatorMock` and adding mocks
- `LinkToken` and Mocks
- Successful Ganache Deployment!
- Python Lottery Scripts/Functions
  - `start_lottery`
  - Brownie tip: Remember to `tx.wait(1)` your last transaction
  - `enter_lottery`
  - `end_lottery`
- Funding with LINK
- brownie interfaces
- Waiting for callback
- Integration Tests & Unit Tests
- Test all lines of code
- `test_get_entrance_fee`
- `pytest.skip` (again)
- `test_cant_enter_unless_started`
- `test_can_start_and_enter_lottery`
- `test_can_pick_winner_correctly`
- Events and Logs
- `callBackWithRandomness`
### Lottery.sol Testnet Deployment
- `topics`
- [conftest.py](https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files)

# ERC20_Practice

- [ERC20/EIP20 Standard](https://eips.ethereum.org/EIPS/eip-20)
- What is an ERC20?
- Creating an ERC20
- [OpenZeppelin ERC20](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20)
- [Solidity 0.8](https://docs.soliditylang.org/en/breaking/080-breaking-changes.html)
- I Challenge you to code this yourself!
- `deploy_token.py`
- Copy paste `helpful_scripts.py`
- Viewing our token in metamask
- Adding to an exchange

# Aave_Brownie

### Defi Intro
- [Defipulse](https://defipulse.com/)
- [Defillama](https://defillama.com/)
- [Aave Testnet Site](https://staging.aave.com/)
- [Paraswap](https://paraswap.io/)
- Decentralized Exchange
### Aave UI
- [Kovan ETH](https://docs.chain.link/docs/link-token-contracts/#kovan)
- What is Aave?
- Borrowing and Lending
- Connecting to Aave
- Depositing Tokens / Lending
- Checking your transaction is correct
- WETH Gateway
- Interest Bearing Token (aToken)
- Collateral
- [DAI](https://makerdao.com/en/)
- [Stablecoin](https://www.investopedia.com/terms/s/stablecoin.asp)
- [Wrapped Bitcoin (wBTC)](https://www.gemini.com/cryptopedia/wrapped-bitcoin-what-can-you-do)
- [Why borrow tokens?](https://docs.aave.com/faq/borrowing)
- [Blockchain Fintech Tutorial](https://blog.chain.link/blockchain-fintech-defi-tutorial-lending-borrowing-python/)
- DISCLAIMER ABOUT BORROWING
- Borrowing Tokens
- [Liquidations](https://docs.aave.com/faq/liquidations)
- Your health factor must be above 1
- [Solvent](https://www.investopedia.com/terms/s/solvency.asp)
- [Stable vs Variable Interest Rate](https://docs.aave.com/faq/borrowing#what-is-the-difference-between-stable-and-variable-rate)
- Repaying our borrows/loans
- Reward token / governance token
- Governance
### [Programmatic Interactions with Aave](https://github.com/PatrickAlphaC/aave_brownie_py_freecode)
- Quant Defi Engineer
- [Aave Documentation](https://docs.aave.com/developers/)
- Setup
- Converting ETH -> WETH
- `get_weth.py`
- [IWETH](https://github.com/PatrickAlphaC/aave_brownie_py/blob/main/interfaces/WethInterface.sol)
- [Kovan WETH Token Address: 0xd0a1e359811322d97991e03f863a0c30c2cf029c](https://kovan.etherscan.io/token/0xd0a1e359811322d97991e03f863a0c30c2cf029c)
- [Mainnet WETH Token Address: 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2](https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2)
- Converting WETH -> ETH with `withdraw`
- `aave_borrow.py`
- [LendingPool](https://docs.aave.com/developers/the-core-protocol/lendingpool)
- [LendingPoolAddressProvider](https://docs.aave.com/developers/the-core-protocol/addresses-provider)
- [LendingPool and LendingPoolAddressProvider Addresses](https://docs.aave.com/developers/deployed-contracts/deployed-contracts)
- Fixing import dependencies
- [Aave Github](https://github.com/aave/protocol-v2)
- [ERC20 Approve Function](https://medium.com/ethex-market/erc20-approve-allow-explained-88d6de921ce9)
- [IERC20 from Patrick's repo](https://github.com/PatrickAlphaC/aave_brownie_py/blob/main/interfaces/IERC20.sol)
- `deposit`
- [getUserAccountData](https://docs.aave.com/developers/the-core-protocol/lendingpool#getuseraccountdata)
- Liquidation Threshold
- [Risk Parameters](https://docs.aave.com/risk/asset-risk/risk-parameters)
- Borrowing DAI 
- Getting DAI Conversion Rate
  - [Chainlink Price Feeds](https://docs.chain.link/docs/reference-contracts/)
  - [AggregatorV3Interface](https://github.com/PatrickAlphaC/aave_brownie_py/blob/main/interfaces/AggregatorV3Interface.sol)
- [borrow](https://docs.aave.com/developers/the-core-protocol/lendingpool#borrow)
- [Mainnet DAI Address: 0x6b175474e89094c44da98b954eedeac495271d0f](https://etherscan.io/token/0x6b175474e89094c44da98b954eedeac495271d0f)
- [Aave Testnet Token Addresses](https://aave.github.io/aave-addresses/kovan.json)
- Repaying
- Kovan Run
- Viewing the transactions

# NFT Contracts Deployment - ERC721

- What is an NFT?
- [ERC721](https://eips.ethereum.org/EIPS/eip-721)
- Token URI
- [Token Metadata Example](https://docs.opensea.io/docs/2-adding-metadata)
- [IPFS](https://ipfs.io/)
### Simple NFT 
- [brownie mix](https://github.com/PatrickAlphaC/nft-mix)
- Initial Setup
- `SimpleCollectible.sol`
- [OpenZeppelin ERC721](https://docs.openzeppelin.com/contracts/3.x/)
- [Pug Image](https://github.com/PatrickAlphaC/nft-mix/blob/main/img/pug.png)
- NFT Constructor
- NFT is a type of factory pattern
- `createCollectible`
  - `_safeMint`
- TokenURI & Metadata
- Opensea listing example
- Is this decentralized?
- Ethereum Size and dStorage
  - [Ethereum Size](https://ycharts.com/indicators/ethereum_chain_full_sync_data_size)
  - [dStorage Solutions](https://ethereum.org/en/developers/docs/storage/)
  - [IPFS](https://www.ipfs.com/)
- You need to have your NFT attributes both on-chain and inside your tokenURI metadata
- `deploy_and_create.py`
- [TokenURI used for the demo: https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json](https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json)
- [IPFS Companion](https://chrome.google.com/webstore/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch?hl=en)
- Rinkeby Deployment
- [Opensea Example](https://testnets.opensea.io/assets/0x8acb7ca932892eb83e4411b59309d44dddbc4cdf/0)
### SimpleCollectible Testing
- What else with NFTs?
### Advanced NFT
- `AdvancedCollectible.sol`
- [Dungeons and Dragons Example](https://github.com/PatrickAlphaC/dungeons-and-dragons-nft)
- Double Inherited Constructors
- `createCollectible` (Advanced)
  - `tokenIdToBreed`
- Working with in-flight Chainlink VRF requests
- Download the NFT images from the [nft-mix](https://github.com/PatrickAlphaC/nft-mix)
- `setTokenURI`
  - `_isApprovedOrOwner`
- Emit events when you update mappings
- [`indexed` event keyword](https://ethereum.stackexchange.com/questions/8658/what-does-the-indexed-keyword-do/8659)
### Advanced deploy_and_create
- Move `OPENSEA_URL` to `helpful_scripts`
- Deploying AdvancedCollectible
  - Opensea testnet is only compatible with Rinkeby
- [Rinkeby Chainlink VRF Contract Addresses](https://docs.chain.link/docs/vrf-contracts/#rinkeby)
- Speeding through adding functions from previous projects
- Deploy to Rinkeby
- `create_collectible.py`
- A quick unit test
- A quick integration test
### Creating Metadata & IPFS
- `create_metadata.py`
- `get_breed`
- Metadata Folder
- `metadata_template`
- NFT Metadata Attributes
- Checking if Metadata file already exists
- Uploading to IPFS
  - `upload_to_ipfs`
  - [Download IPFS Command Line](https://docs.ipfs.io/install/command-line/)
  - [Download IPFS Desktop](https://docs.ipfs.io/install/ipfs-desktop/)
  - [HTTP IPFS Docs](https://docs.ipfs.io/reference/http/api/)
  - `ipfs daemon`
  - [Pinata](https://app.pinata.cloud/)
  - [Pinata Docs](https://docs.pinata.cloud/)
  - Refactoring to not re-upload to IPFS
- Setting the TokenURI
- End-To-End Manual Testnet Test
- Viewing on Opensea

# Smart Contract Upgrades

### Introduction to upgrading smart contracts
- [Original Video](https://www.youtube.com/watch?v=bdXJmWajZRY)
- Smart Contracts can be upgraded!
- Does this mean they are not immutable? 
- [Trail of Bits on Upgradeable Smart Contracts](https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/)
- The "Not Really Upgrading" / Parameterization Method
- The Social Yeet / Migration Method
- [Contract Migration](https://blog.trailofbits.com/2018/10/29/how-contract-migration-works/)
- Proxies
  - DelegateCall
  - Terminology:
    - Implementation Contract
    - Proxy Contract
    - User
    - Admin
  - Gotchas:
    - Storage Clashes
    - Function Selector
    - Function Selector Clashes
  - Proxy Patterns:
    - [Transparent Proxy Pattern](https://blog.openzeppelin.com/the-transparent-proxy-pattern/)
    - [Universal Upgrade Proxy Standard](https://eips.ethereum.org/EIPS/eip-1822)
    - [Diamond/Multi-Facet Proxy](https://eips.ethereum.org/EIPS/eip-2535)
### Upgrades-mix and code
- Setup
- `Box.sol`
- `BoxV2.sol`
- Getting the proxy contracts
- [Openzeppelin Proxy Github](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts/proxy/transparent)
- `01_deploy_box.py`
- Hooking up a proxy to our implementation contract
- (Optional) [Creating a Gnosis Safe](https://help.gnosis-safe.io/en/articles/3876461-create-a-safe)
- Initializers
- Encoding Initializer Function
- Assigning ABI to a proxy
- Running the script
- Upgrade Python Function
### Testing Upgrades
- Testing our proxy
- Testing our upgrades

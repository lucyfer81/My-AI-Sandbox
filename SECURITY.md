# Security Notice

## API Credentials Security

This repository uses **environment variables and GitHub Secrets** for sensitive credentials. No actual API keys are hardcoded in the source code.

### What You'll Find in the Code
- **Placeholder strings** like `REPLACE_WITH_YOUR_TENCENT_SECRET_ID` - these are NOT real secrets
- **Environment variable references** like `${{ secrets.TENCENT_SECRET_ID }}` - these use GitHub's secure secret storage
- **Configuration templates** that show users where to place their own credentials

### Security Best Practices
1. **Never commit actual API keys** to the repository
2. **Use GitHub Secrets** for CI/CD workflows
3. **Use environment variables** for local development
4. **Replace placeholders** with your actual credentials when setting up locally

### Setting Up Credentials
See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions on securely configuring API credentials.

### False Positive Warnings
Some security scanning tools may flag our placeholder strings as potential secrets. These are false positives - the actual values are always placeholders like `REPLACE_WITH_YOUR_TENCENT_SECRET_ID`.
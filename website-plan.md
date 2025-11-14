# Website Plan - awsaavedra.github.io

## Email Subscription & Newsletter Strategy

### Current Implementation (Derek Sivers Style)

The website uses a simple, human-centric newsletter approach inspired by Derek Sivers:

#### Subscription Form
- **Location**: Footer of every page
- **Fields**: Email + Math challenge (anti-bot)
- **Validation**: 
  - HTML5 email type
  - Strict regex pattern (RFC 5322 compliant)
  - Pattern: `^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$`
- **Anti-bot Protection**:
  - Random math problem (generated at build time, changes with each deployment)
  - Dropdown selection (harder for bots than text input)
  - No JavaScript required

#### Newsletter System
- **Single Tier**: One list for article publication notifications only
- **Event Trigger**: New article published
- **Frequency**: As articles are published (irregular, manual)
- **Philosophy**: Simple notifications, no segmentation or frequency tiers

#### Subscriber Management
- **Script**: `manage-subscribers.py`
- **Storage**: `newsletter/subscribers.txt` (plain text, one email per line)
- **Commands**:
  - `add <email>` - Add subscriber (after manual verification)
  - `remove <email>` - Remove subscriber
  - `list` - Show all subscribers
  - `export <file.csv>` - Export to CSV (for Listmonk import)

#### Newsletter Sending
- **Script**: `send-newsletter.py`
- **SMTP**: Configured for smtp2go.com (or any SMTP relay)
- **Format**: Plain-text emails only (no HTML templates)
- **Features**:
  - Dry-run mode for preview
  - Automatic unsubscribe footer
  - Rate limiting (0.5s between emails)
  - Manual sending triggered by new article publication

#### Listmonk Integration
- **Method**: Manual CSV import (Option 3)
- **Script**: `export-to-listmonk.py`
- **Workflow**:
  1. Export subscribers to CSV format
  2. Log into Listmonk admin panel
  3. Import CSV via Subscribers → Import
  4. Map columns: email, name, status
  5. Use Listmonk for sending (optional, or stick with Python scripts)

### Email Validation Strategy

#### What We Do (Client-Side)
1. **Format Validation**: Strict regex catches obvious typos and invalid formats
2. **Bot Prevention**: Math challenge blocks automated submissions
3. **Required Fields**: HTML5 validation ensures completeness

#### What We Can't Do (Without Backend)
- Verify email actually exists
- Check DNS/MX records
- Detect disposable email services
- Verify mailbox is active

#### Recommended Workflow (Manual Quality Control)

**Best Practice: Double Opt-In Process**

1. **Form Submission**: User submits via Netlify Forms
2. **Notification**: You receive email notification from Netlify
3. **Manual Review**: Check submission for obvious spam/typos
4. **Personal Welcome**: Send welcome email from your personal address
   ```
   Subject: Welcome! Confirm your subscription
   
   Hi there,
   
   Thanks for subscribing to my article notifications. 
   Just reply to this email to confirm you want to hear from me.
   
   You'll get an email whenever I publish a new article.
   
   - Alex
   ```
5. **Confirmation**: Only add to newsletter list after they reply
6. **Add to List**: Use `python newsletter/manage-subscribers.py add email@example.com`

**Why This Approach?**
- ✅ Ensures real, engaged subscribers
- ✅ GDPR/CAN-SPAM compliant
- ✅ Maintains personal, human connection
- ✅ No additional services or costs
- ✅ Filters out typos and fake emails naturally
- ✅ Aligns with Derek Sivers philosophy

#### Alternative: Automated Services (Not Recommended)

Could use services like:
- ZeroBounce, NeverBounce, EmailListVerify
- Downsides: Costs money, privacy concerns, adds complexity

**Decision**: Stick with manual verification for simplicity and quality

### Newsletter Trigger & Frequency

**Single Event Trigger: New Article Publication**

- **When**: Only when a new article is published
- **What**: Email notification with link to article
- **Who**: All subscribers (single list, no segmentation)
- **How Often**: Irregular - depends on article publication schedule

**No Automated Scheduling** - Each newsletter is manually sent after publishing an article.

### Content Philosophy

**Keep It Simple, Personal, Human**
- Plain-text only (no fancy HTML templates)
- Write like you're emailing a friend
- Article notification format:
  - Brief introduction
  - Link to new article
  - Optional context or highlights
- Direct, concise, valuable
- Easy unsubscribe (just reply)

### Technical Stack

- **Static Site**: Hugo
- **Theme**: hugo-bearblog (customized)
- **Hosting**: GitHub Pages / Netlify
- **Forms**: Netlify Forms
- **Email Sending**: SMTP relay (smtp2go.com or similar)
- **Subscriber Storage**: Plain text file (`newsletter/subscribers.txt`)
- **Management**: Python scripts (no database needed)
- **Optional**: Listmonk (manual CSV import for advanced features)

### File Structure

```
newsletter/
├── subscribers.txt           # Single list of all subscribers
├── manage-subscribers.py     # Add/remove/list/export subscribers
├── send-newsletter.py        # Send article notifications
└── export-to-listmonk.py     # Export CSV for Listmonk import
```

### Future Considerations

#### Maybe Later
- [ ] RSS feed promotion
- [ ] Archive page with browser search (Ctrl+F)
- [ ] Automated welcome sequence
- [ ] Analytics (simple, privacy-focused)
- [ ] Full Listmonk integration (if subscriber base grows)
- [ ] Automated article detection (RSS-to-email)

#### Probably Never
- ❌ Fancy email templates (keep it plain text)
- ❌ Marketing automation (stay personal)
- ❌ Email verification APIs (manual is fine)
- ❌ Tracking pixels (respect privacy)
- ❌ A/B testing (overthinking it)
- ❌ Multiple subscriber tiers (keep it simple)

### SMTP Configuration

Set environment variables:
```bash
export SMTP_HOST="smtp2go.com"
export SMTP_PORT="2525"
export SMTP_USERNAME="your_username"
export SMTP_PASSWORD="your_password"
export FROM_EMAIL="your@email.com"
export FROM_NAME="Alexander Saavedra"
```

Or edit directly in `send-newsletter.py`

### Usage Examples

**Complete Workflow: From Submission to Newsletter**

1. **Check Netlify form submissions**:
   - Log into Netlify dashboard
   - Go to Forms → subscribe
   - Review new submissions

2. **Manually verify subscriber** (double opt-in):
   - Send personal welcome email
   - Wait for confirmation reply
   - Only proceed after confirmation

3. **Add confirmed subscriber**:
   ```bash
   cd newsletter
   python manage-subscribers.py add john@example.com
   ```

4. **List all subscribers**:
   ```bash
   python manage-subscribers.py list
   ```

5. **When publishing new article**, create message file (`new-article.txt`):
   ```
   Subject: New article: Title of Your Article
   
   Hi there,
   
   I just published a new article about [topic].
   
   Read it here: https://awsaavedra.com/posts/article-name/
   
   Hope you enjoy it!
   
   - Alex
   ```

6. **Preview newsletter** (dry-run):
   ```bash
   python send-newsletter.py new-article.txt --dry-run
   ```

7. **Send newsletter to all subscribers**:
   ```bash
   python send-newsletter.py new-article.txt
   ```

8. **Optional: Export to Listmonk** (for advanced features):
   ```bash
   python export-to-listmonk.py
   # Then manually import CSV into Listmonk admin panel
   ```

### Privacy & Legal

- No tracking pixels
- No third-party analytics on emails
- Clear unsubscribe method (reply to email)
- Manual list management (full control)
- Emails stored in private git repo
- No sharing subscriber data

---

## Site Features

### Implemented
- [x] LaTeX math rendering (Hugo native, no JavaScript)
- [x] Newsletter subscription (Derek Sivers style, single tier)
- [x] Email validation (regex + manual verification)
- [x] Disclaimer page (health & financial)
- [x] Custom fonts (Scriptin for title)
- [x] Social icons (GitHub, LinkedIn)
- [x] Copyright notice
- [x] Article notification system (single list)
- [x] Listmonk export capability (manual CSV import)

### TODO
- [ ] Complete end-to-end newsletter test (dry-run → real send)
- [ ] Configure SMTP environment variables
- [ ] RSS feed setup and promotion
- [ ] Archive/search page (browser Ctrl+F)
- [ ] Monetization strategy

---

*Last updated: 2025-11-13*

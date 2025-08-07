-- Initialize Twikoo database tables

-- Comments table
CREATE TABLE IF NOT EXISTS comment (
    _id TEXT PRIMARY KEY,
    uid TEXT,
    nick TEXT,
    mail TEXT,
    mailMd5 TEXT,
    link TEXT,
    ua TEXT,
    ip TEXT,
    master INTEGER DEFAULT 0,
    url TEXT,
    href TEXT,
    comment TEXT,
    pid TEXT,
    rid TEXT,
    isSpam INTEGER DEFAULT 0,
    created INTEGER,
    updated INTEGER,
    like TEXT DEFAULT '[]',
    top INTEGER DEFAULT 0,
    avatar TEXT
);

-- Counter table
CREATE TABLE IF NOT EXISTS counter (
    url TEXT PRIMARY KEY,
    title TEXT,
    time INTEGER DEFAULT 0,
    created INTEGER,
    updated INTEGER
);

-- Config table
CREATE TABLE IF NOT EXISTS config (
    value TEXT
);

-- Insert default empty config
INSERT INTO config (value) VALUES ('{}');

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_comment_url ON comment(url);
CREATE INDEX IF NOT EXISTS idx_comment_rid ON comment(rid);
CREATE INDEX IF NOT EXISTS idx_comment_created ON comment(created);
CREATE INDEX IF NOT EXISTS idx_comment_isSpam ON comment(isSpam);
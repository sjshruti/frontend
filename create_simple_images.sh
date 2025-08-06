#!/bin/bash

# Create assets directory
mkdir -p assets

# Create simple HTML files that can serve as placeholders
cat > assets/profile.jpg.html << 'HTMLEOF'
<!DOCTYPE html>
<html><body style="margin:0;width:400px;height:400px;background:linear-gradient(135deg,#F8BBD9,#DDD6FE);display:flex;align-items:center;justify-content:center;font-family:Arial;font-size:24px;color:#333;">
<div style="text-align:center;">
<h2>Shruti Jayaswal</h2>
<p>Profile Photo</p>
</div>
</body></html>
HTMLEOF

echo "Created placeholder structure for images"
echo "Note: Replace these with actual photos later"

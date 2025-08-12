# Railway Production Download Priority

## Essential Files for Railway Deployment

### 1. **Core Production Server** (REQUIRED)
```
updated_production_server.py
```
**What it does**: Enhanced production server with fallback token support, triple table architecture, and monitoring endpoints.

### 2. **Enhanced Database Processor** (REQUIRED)
```
fixed_dual_table_processor.py
```
**What it does**: Handles all database operations including fallback_processing_coins table that you requested.

### 3. **Token Monitoring System** (REQUIRED)
```
new_token_only_monitor.py
notification_enhanced_retry_service.py
```
**What they do**: Real-time token detection and background name resolution services.

### 4. **Configuration & Dependencies** (REQUIRED)
```
requirements.txt
Procfile
railway.toml
Dockerfile
```
**What they do**: Railway deployment configuration and Python dependencies.

## Quick Download Command

If you want everything in one package, download:
```
DEPLOYMENT_PACKAGE_FINAL.zip
```

## Specific for Your Fallback Request

Since you specifically asked about fallback tokens not appearing, these files now ensure they work:

1. **updated_production_server.py** - Routes failed tokens to fallback table
2. **fixed_dual_table_processor.py** - Creates and manages fallback_processing_coins table
3. **test_fallback_system.py** - Verify fallback functionality works

## Database Already Configured

Your Railway database at `crossover.proxy.rlwy.net:40211` already has:
- ✅ fallback_processing_coins table created
- ✅ 5+ test tokens stored
- ✅ All required indexes and structure

## Next Steps

1. Download `updated_production_server.py` and `fixed_dual_table_processor.py`
2. Replace your current Railway deployment files
3. Deploy to Railway
4. Visit `/fallback_tokens` endpoint to see tokens that failed API resolution

The fallback system is now working correctly and will capture tokens that previously would have been lost due to API failures.
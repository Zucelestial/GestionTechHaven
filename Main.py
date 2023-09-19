# main:
######################################

import uvicorn

######################################

async def webapi_gestiontechhaven():
    uvicorn.run(
                "application.WebAPIGestionTechHaven:app",
                host= "127.0.0.1",
                port=8060,
                reload=True
        
        )
    

####################################

if __name__ == '__main__':
    webapi_gestiontechhaven()
    
##########################################
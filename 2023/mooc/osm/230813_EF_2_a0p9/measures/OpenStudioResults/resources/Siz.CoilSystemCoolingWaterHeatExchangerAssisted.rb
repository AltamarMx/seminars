# *******************************************************************************
# OpenStudio(R), Copyright (c) Alliance for Sustainable Energy, LLC.
# See also https://openstudio.net/license
# *******************************************************************************

class OpenStudio::Model::CoilSystemCoolingWaterHeatExchangerAssisted
  def performanceCharacteristics
    effs = []
    effs += coolingCoil.performanceCharacteristics
    return effs
  end
end

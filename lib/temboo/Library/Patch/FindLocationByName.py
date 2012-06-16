
###############################################################################
#
# FindLocationByName
# Return Patch location information for a specified U.S. region.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FindLocationByName(Choreography):

    """
    Create a new instance of the FindLocationByName Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Patch/FindLocationByName')


    def new_input_set(self):
        return FindLocationByNameInputSet()

    def _make_result_set(self, result, path):
        return FindLocationByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindLocationByNameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FindLocationByName
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FindLocationByNameInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) A valid API key provided by Patch.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) The API shared secret provided by Patch.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Specify a maximum number of locations to return, between 1 and 100. The default is 10.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the RegionName input for this choreography. ((required, string) Enter a state, city, neighborhood, district (county), locality (borough), or metro area name; a place name, such as a business, landmark, or park; or a ZIP code. Separate multiple names with commas.)
        """
        def set_RegionName(self, value):
            InputSet._set_input(self, 'RegionName', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Specify "xml" to convert the Patch JSON response to XML, or "json" (the default) to not convert.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the FindLocationByName choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FindLocationByNameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response returned from Patch.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Coordinates" output from this choreography execution. ((string) The concatenated location latitude and longitude returned by Patch.)
        """
        def get_Coordinates(self):
            return self._output.get('Coordinates', None)
        """
        Retrieve the value for the "Latitude" output from this choreography execution. ((decimal) The latitude for the location returned by Patch.)
        """
        def get_Latitude(self):
            return self._output.get('Latitude', None)
        """
        Retrieve the value for the "LocationID" output from this choreography execution. ((string) )
        """
        def get_LocationID(self):
            return self._output.get('LocationID', None)
        """
        Retrieve the value for the "Longitude" output from this choreography execution. ((decimal) The longitude for the location returned by Patch.)
        """
        def get_Longitude(self):
            return self._output.get('Longitude', None)

class FindLocationByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindLocationByNameResultSet(response, path)


###############################################################################
#
# ConvertXMLToBase64EncodedExcel
# Converts an XML file to a Base64 encoded Excel file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertXMLToBase64EncodedExcel(Choreography):

    """
    Create a new instance of the ConvertXMLToBase64EncodedExcel Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/DataConversions/ConvertXMLToBase64EncodedExcel')


    def new_input_set(self):
        return ConvertXMLToBase64EncodedExcelInputSet()

    def _make_result_set(self, result, path):
        return ConvertXMLToBase64EncodedExcelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertXMLToBase64EncodedExcelChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertXMLToBase64EncodedExcel
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertXMLToBase64EncodedExcelInputSet(InputSet):
        """
        Set the value of the XMLFile input for this choreography. ((required, xml) The XML file you want to convert to XLS format. See documentation for information on the required XML schema.)
        """
        def set_XMLFile(self, value):
            InputSet._set_input(self, 'XMLFile', value)


"""
A ResultSet with methods tailored to the values returned by the ConvertXMLToBase64EncodedExcel choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertXMLToBase64EncodedExcelResultSet(ResultSet):
        """
        Retrieve the value for the "ExcelFile" output from this choreography execution. (The Base64 encoded Excel data .)
        """
        def get_ExcelFile(self):
            return self._output.get('ExcelFile', None)

class ConvertXMLToBase64EncodedExcelChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertXMLToBase64EncodedExcelResultSet(response, path)

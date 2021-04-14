<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyAlgorithm="0" simplifyMaxScale="1" simplifyDrawingHints="0" simplifyDrawingTol="1" labelsEnabled="0" version="3.12.3-București" minScale="100000000" simplifyLocal="1" readOnly="0" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" type="RuleRenderer" forceraster="0" enableorderby="0">
    <rules key="{00763c6a-cdb4-4069-9651-a6e4307a9114}">
      <rule filter="liikenne_hlo_tco2 > liikenne_palv_tco2 AND liikenne_hlo_tco2 > liikenne_tv_tco2" symbol="0" key="{373d3f4d-e447-48e7-885d-655b86bd432d}" label="Henkilöliikenne"/>
      <rule filter="liikenne_palv_tco2 > liikenne_hlo_tco2 AND liikenne_palv_tco2 > liikenne_tv_tco2" symbol="1" key="{c5334ae7-6514-4083-b802-934428dce548}" label="Palvelurakennusten liikenne"/>
      <rule filter="liikenne_tv_tco2 > liikenne_palv_tco2 AND liikenne_tv_tco2 > liikenne_hlo_tco2" symbol="2" key="{81a4aa42-e878-43e1-b0b8-e5f3530bb4a3}" label="Teeollisuus- ja&#xa;varastorakennusten liikenne"/>
    </rules>
    <symbols>
      <symbol type="fill" name="0" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer enabled="1" pass="0" class="CentroidFill" locked="0">
          <prop v="0" k="point_on_all_parts"/>
          <prop v="0" k="point_on_surface"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@0" alpha="1" force_rhr="0" clip_to_extent="1">
            <layer enabled="1" pass="0" class="SimpleMarker" locked="0">
              <prop v="0" k="angle"/>
              <prop v="255,78,0,0" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="square" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="Pixel" k="offset_unit"/>
              <prop v="220,12,203,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.4" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="fill" name="1" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer enabled="1" pass="0" class="CentroidFill" locked="0">
          <prop v="0" k="point_on_all_parts"/>
          <prop v="0" k="point_on_surface"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@1@0" alpha="1" force_rhr="0" clip_to_extent="1">
            <layer enabled="1" pass="0" class="SimpleMarker" locked="0">
              <prop v="0" k="angle"/>
              <prop v="0,0,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="triangle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="Pixel" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="1" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="Pixel" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1.6" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="fill" name="2" alpha="1" force_rhr="0" clip_to_extent="1">
        <layer enabled="1" pass="0" class="CentroidFill" locked="0">
          <prop v="0" k="point_on_all_parts"/>
          <prop v="0" k="point_on_surface"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@2@0" alpha="1" force_rhr="0" clip_to_extent="1">
            <layer enabled="1" pass="0" class="SimpleMarker" locked="0">
              <prop v="0" k="angle"/>
              <prop v="170,0,255,0" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="Pixel" k="offset_unit"/>
              <prop v="75,75,75,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.4" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1.2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions" value="fid"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <LinearlyInterpolatedDiagramRenderer classificationAttributeExpression=" &quot;vesi_tco2&quot; + &quot;lammitys_tco2&quot; + &quot;jaahdytys_tco2&quot; + &quot;kiinteistosahko_tco2&quot; + &quot;sahko_kotitaloudet_tco2&quot; + &quot;sahko_palv_tco2&quot; + &quot;sahko_tv_tco2&quot; + &quot;hloliikenne_ap_tco2&quot; + &quot;hloliikenne_tp_tco2&quot; + &quot;tvliikenne_tco2&quot; + &quot;palvliikenne_tco2&quot; + &quot;korjaussaneeraus_tco2&quot; " upperHeight="10" attributeLegend="1" upperWidth="10" lowerWidth="0" diagramType="Pie" lowerValue="0" upperValue="12138.6" lowerHeight="0">
    <DiagramCategory sizeType="MM" backgroundColor="#ffffff" minScaleDenominator="1000" penWidth="0.1" lineSizeType="MM" maxScaleDenominator="50000" opacity="1" scaleDependency="Area" sizeScale="3x:0,0,0,0,0,0" width="15" showAxis="0" lineSizeScale="3x:0,0,0,0,0,0" spacingUnit="MM" height="15" spacing="0" direction="1" barWidth="5" penAlpha="255" penColor="#ffffff" minimumSize="3" backgroundAlpha="255" scaleBasedVisibility="1" rotationOffset="270" spacingUnitScale="3x:0,0,0,0,0,0" enabled="0" labelPlacementMethod="XHeight" diagramOrientation="Up">
      <fontProperties style="" description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0"/>
      <attribute color="#ca4d41" field="lammitys_tco2" label="Lämmitys"/>
      <attribute color="#418aca" field="vesi_tco2" label="Vesi"/>
      <attribute color="#c551bc" field="hloliikenne_ap_tco2" label="Henkilöliikenne, ap"/>
      <attribute color="#ecff3b" field="sahko_kotitaloudet_tco2" label="Sähkö, kotitaloudet"/>
      <attribute color="#745d7c" field="palvliikenne_tco2" label="Palveluliikenne"/>
      <attribute color="#decd98" field="sahko_palv_tco2" label="Sähkö, palvelut"/>
      <attribute color="#661f98" field="tvliikenne_tco2" label="Liikenne, tv"/>
      <attribute color="#bbf7d6" field="sahko_tv_tco2" label="Sähkö, tv"/>
      <attribute color="#3a2f6c" field="kiinteistosahko_tco2" label="Kiinteistösähkö"/>
      <attribute color="#4dee3b" field="hloliikenne_tp_tco2" label="Henkilöliikenne, tp"/>
      <attribute color="#d6a4ff" field="korjaussaneeraus_tco2" label="Korjaussaneeraus"/>
      <attribute color="#51c7bc" field="jaahdytys_tco2" label="Jäähdytys"/>
      <axisSymbol>
        <symbol type="line" name="" alpha="1" force_rhr="0" clip_to_extent="1">
          <layer enabled="1" pass="0" class="SimpleLine" locked="0">
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </LinearlyInterpolatedDiagramRenderer>
  <DiagramLayerSettings placement="4" linePlacementFlags="18" zIndex="0" showAll="1" priority="10" dist="0" obstacle="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" name="allowedGapsBuffer" value="0"/>
        <Option type="bool" name="allowedGapsEnabled" value="false"/>
        <Option type="QString" name="allowedGapsLayer" value=""/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="xyind">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="vyohyke">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="asukkaat">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tp_yht_2017">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="vuosi">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_liikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2_per_asukas">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2_per_tp_yht">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2_per_asukas_tp_yht">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2_per_sum_liikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2_per_sum_yhteensa_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_liikenne_tco2_per_sum_yhteensa_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="id" index="0"/>
    <alias name="" field="xyind" index="1"/>
    <alias name="" field="vyohyke" index="2"/>
    <alias name="" field="asukkaat" index="3"/>
    <alias name="" field="tp_yht_2017" index="4"/>
    <alias name="" field="vuosi" index="5"/>
    <alias name="" field="liikenne_hlo_tco2" index="6"/>
    <alias name="" field="liikenne_tv_tco2" index="7"/>
    <alias name="" field="liikenne_palv_tco2" index="8"/>
    <alias name="" field="sum_liikenne_tco2" index="9"/>
    <alias name="" field="liikenne_hlo_tco2_per_asukas" index="10"/>
    <alias name="" field="liikenne_hlo_tco2_per_tp_yht" index="11"/>
    <alias name="" field="liikenne_hlo_tco2_per_asukas_tp_yht" index="12"/>
    <alias name="" field="liikenne_hlo_tco2_per_sum_liikenne_tco2" index="13"/>
    <alias name="" field="sum_yhteensa_tco2" index="14"/>
    <alias name="" field="liikenne_hlo_tco2_per_sum_yhteensa_tco2" index="15"/>
    <alias name="" field="sum_liikenne_tco2_per_sum_yhteensa_tco2" index="16"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="id" expression="" applyOnUpdate="0"/>
    <default field="xyind" expression="" applyOnUpdate="0"/>
    <default field="vyohyke" expression="" applyOnUpdate="0"/>
    <default field="asukkaat" expression="" applyOnUpdate="0"/>
    <default field="tp_yht_2017" expression="" applyOnUpdate="0"/>
    <default field="vuosi" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2" expression="" applyOnUpdate="0"/>
    <default field="liikenne_tv_tco2" expression="" applyOnUpdate="0"/>
    <default field="liikenne_palv_tco2" expression="" applyOnUpdate="0"/>
    <default field="sum_liikenne_tco2" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2_per_asukas" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2_per_tp_yht" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2_per_asukas_tp_yht" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2_per_sum_liikenne_tco2" expression="" applyOnUpdate="0"/>
    <default field="sum_yhteensa_tco2" expression="" applyOnUpdate="0"/>
    <default field="liikenne_hlo_tco2_per_sum_yhteensa_tco2" expression="" applyOnUpdate="0"/>
    <default field="sum_liikenne_tco2_per_sum_yhteensa_tco2" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" notnull_strength="1" constraints="3" exp_strength="0" field="id"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="xyind"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="vyohyke"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="asukkaat"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="tp_yht_2017"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="vuosi"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_tv_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_palv_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="sum_liikenne_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2_per_asukas"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2_per_tp_yht"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2_per_asukas_tp_yht"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2_per_sum_liikenne_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="sum_yhteensa_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="liikenne_hlo_tco2_per_sum_yhteensa_tco2"/>
    <constraint unique_strength="0" notnull_strength="0" constraints="0" exp_strength="0" field="sum_liikenne_tco2_per_sum_yhteensa_tco2"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="id" desc=""/>
    <constraint exp="" field="xyind" desc=""/>
    <constraint exp="" field="vyohyke" desc=""/>
    <constraint exp="" field="asukkaat" desc=""/>
    <constraint exp="" field="tp_yht_2017" desc=""/>
    <constraint exp="" field="vuosi" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2" desc=""/>
    <constraint exp="" field="liikenne_tv_tco2" desc=""/>
    <constraint exp="" field="liikenne_palv_tco2" desc=""/>
    <constraint exp="" field="sum_liikenne_tco2" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2_per_asukas" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2_per_tp_yht" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2_per_asukas_tp_yht" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2_per_sum_liikenne_tco2" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2_per_sum_yhteensa_tco2" desc=""/>
    <constraint exp="" field="sum_liikenne_tco2_per_sum_yhteensa_tco2" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;liikenne_tv_tco2&quot;" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column hidden="0" width="-1" type="field" name="xyind"/>
      <column hidden="0" width="81" type="field" name="vuosi"/>
      <column hidden="1" width="-1" type="actions"/>
      <column hidden="0" width="121" type="field" name="liikenne_hlo_tco2"/>
      <column hidden="0" width="119" type="field" name="liikenne_tv_tco2"/>
      <column hidden="0" width="129" type="field" name="liikenne_palv_tco2"/>
      <column hidden="0" width="176" type="field" name="sum_yhteensa_tco2"/>
      <column hidden="0" width="140" type="field" name="sum_liikenne_tco2"/>
      <column hidden="0" width="-1" type="field" name="asukkaat"/>
      <column hidden="0" width="-1" type="field" name="id"/>
      <column hidden="0" width="-1" type="field" name="vyohyke"/>
      <column hidden="0" width="-1" type="field" name="tp_yht_2017"/>
      <column hidden="0" width="-1" type="field" name="liikenne_hlo_tco2_per_asukas"/>
      <column hidden="0" width="-1" type="field" name="liikenne_hlo_tco2_per_tp_yht"/>
      <column hidden="0" width="-1" type="field" name="liikenne_hlo_tco2_per_asukas_tp_yht"/>
      <column hidden="0" width="-1" type="field" name="liikenne_hlo_tco2_per_sum_liikenne_tco2"/>
      <column hidden="0" width="-1" type="field" name="liikenne_hlo_tco2_per_sum_yhteensa_tco2"/>
      <column hidden="0" width="-1" type="field" name="sum_liikenne_tco2_per_sum_yhteensa_tco2"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="asukkaat"/>
    <field editable="1" name="fid"/>
    <field editable="1" name="hloliikenne_ap_tco2"/>
    <field editable="1" name="hloliikenne_tp_tco2"/>
    <field editable="1" name="id"/>
    <field editable="1" name="id_0"/>
    <field editable="1" name="jaahdytys_tco2"/>
    <field editable="1" name="kiinteistosahko_tco2"/>
    <field editable="1" name="korjaussaneeraus_tco2"/>
    <field editable="1" name="lammitys_tco2"/>
    <field editable="1" name="liikenne_hlo_tco2"/>
    <field editable="1" name="liikenne_hlo_tco2_per_asukas"/>
    <field editable="1" name="liikenne_hlo_tco2_per_asukas_tp_yht"/>
    <field editable="1" name="liikenne_hlo_tco2_per_sum_liikenne_tco2"/>
    <field editable="1" name="liikenne_hlo_tco2_per_sum_yhteensa_tco2"/>
    <field editable="1" name="liikenne_hlo_tco2_per_tp_yht"/>
    <field editable="1" name="liikenne_palv_tco2"/>
    <field editable="1" name="liikenne_tv_tco2"/>
    <field editable="1" name="liikenne_yht"/>
    <field editable="1" name="palvliikenne_tco2"/>
    <field editable="1" name="rak_korjaussaneeraus_tco2"/>
    <field editable="1" name="rak_purku_tco2"/>
    <field editable="1" name="rak_uudis_tco2"/>
    <field editable="1" name="sahko_kiinteistot_tco2"/>
    <field editable="1" name="sahko_kotitaloudet_tco2"/>
    <field editable="1" name="sahko_palv_tco2"/>
    <field editable="1" name="sahko_tv_tco2"/>
    <field editable="1" name="sahko_yht"/>
    <field editable="1" name="sum_lammonsaato_tco2"/>
    <field editable="1" name="sum_liikenne_tco2"/>
    <field editable="1" name="sum_liikenne_tco2_per_sum_yhteensa_tco2"/>
    <field editable="1" name="sum_rakentaminen_tco2"/>
    <field editable="1" name="sum_sahko_tco2"/>
    <field editable="1" name="sum_yhteensa_tco2"/>
    <field editable="1" name="summa"/>
    <field editable="1" name="tilat_jaahdytys_tco2"/>
    <field editable="1" name="tilat_lammitys_tco2"/>
    <field editable="1" name="tilat_vesi_tco2"/>
    <field editable="1" name="tp_yht_2017"/>
    <field editable="1" name="tvliikenne_tco2"/>
    <field editable="1" name="vesi_tco2"/>
    <field editable="1" name="vuosi"/>
    <field editable="1" name="vyohyke"/>
    <field editable="1" name="xyind"/>
  </editable>
  <labelOnTop>
    <field name="asukkaat" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="hloliikenne_ap_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tp_tco2" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="id_0" labelOnTop="0"/>
    <field name="jaahdytys_tco2" labelOnTop="0"/>
    <field name="kiinteistosahko_tco2" labelOnTop="0"/>
    <field name="korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="lammitys_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2_per_asukas" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2_per_asukas_tp_yht" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2_per_sum_liikenne_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2_per_sum_yhteensa_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2_per_tp_yht" labelOnTop="0"/>
    <field name="liikenne_palv_tco2" labelOnTop="0"/>
    <field name="liikenne_tv_tco2" labelOnTop="0"/>
    <field name="liikenne_yht" labelOnTop="0"/>
    <field name="palvliikenne_tco2" labelOnTop="0"/>
    <field name="rak_korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="rak_purku_tco2" labelOnTop="0"/>
    <field name="rak_uudis_tco2" labelOnTop="0"/>
    <field name="sahko_kiinteistot_tco2" labelOnTop="0"/>
    <field name="sahko_kotitaloudet_tco2" labelOnTop="0"/>
    <field name="sahko_palv_tco2" labelOnTop="0"/>
    <field name="sahko_tv_tco2" labelOnTop="0"/>
    <field name="sahko_yht" labelOnTop="0"/>
    <field name="sum_lammonsaato_tco2" labelOnTop="0"/>
    <field name="sum_liikenne_tco2" labelOnTop="0"/>
    <field name="sum_liikenne_tco2_per_sum_yhteensa_tco2" labelOnTop="0"/>
    <field name="sum_rakentaminen_tco2" labelOnTop="0"/>
    <field name="sum_sahko_tco2" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2" labelOnTop="0"/>
    <field name="summa" labelOnTop="0"/>
    <field name="tilat_jaahdytys_tco2" labelOnTop="0"/>
    <field name="tilat_lammitys_tco2" labelOnTop="0"/>
    <field name="tilat_vesi_tco2" labelOnTop="0"/>
    <field name="tp_yht_2017" labelOnTop="0"/>
    <field name="tvliikenne_tco2" labelOnTop="0"/>
    <field name="vesi_tco2" labelOnTop="0"/>
    <field name="vuosi" labelOnTop="0"/>
    <field name="vyohyke" labelOnTop="0"/>
    <field name="xyind" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
